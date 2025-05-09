# -*- coding: utf-8 -*-
'''
Rec Engine
Notebook #2

This notebook reads in the initial parquet file, filters out the datasets that do not have a landing page link,
then iterates through the datasets with landing pages to determine if they match the potential URL Socrata formats.
Those that do are then scraped using the Socrata API to get information about the dataset's features.

As over 100,000 records were added to the parquet file in the previous step, this notebook was written and executed using pyspark in Databricks.
'''

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pyspark.sql import SparkSession
from pyspark.sql.functions import substring, col, to_date, year, month, coalesce
import json, os, requests, re
import pyspark.sql.functions as F

#create spark session
spark = SparkSession.builder.appName('EDA').getOrCreate()

#read parquet data file
file = 'dbfs:/user/hive/warehouse/open_data.parquet'
df = spark.read.format('parquet').load(file)

#count the number of rows in the dataframe
record_count = df.count()

#create table of just ID, name, and landing page
df_socrata = df.select('id', 'landing_page', 'name')

display(df_socrata)

#check for nulls in the socrata dataframe
socrata_null = df_socrata.select(F.sum(col('landing_page').isNull().cast('int'))).collect()[0][0]

#calculate how many records in socrata dataframe have null for landing page
print(f'{socrata_null/record_count:.2%} of datasets do not have a landing page linked.')

#split the socrata dataframe into two - one for nulls, one for non-nulls
no_lp_socrata = df_socrata.filter(df_socrata['landing_page'].isNull())
df_lp_socrata = df_socrata.filter(df_socrata['landing_page'].isNotNull())

print(no_lp_socrata.count())

print(len(df_lp_socrata_pd))

#convert non-null df to pandas
df_lp_socrata_pd = df_lp_socrata.toPandas()

display(df_lp_socrata)

df_lp_socrata_pd.to_csv('/dbfs/user/hive/warehouse/df_lp_socrata.csv', index=False)

directory = '/dbfs/user/hive/warehouse'
if not os.path.exists(directory):
    os.makedirs(directory)

#create path for socrata data
socrata_file = '/dbfs/user/hive/warehouse/socrata_metadata.csv'

#1. load existing file if it exists
if os.path.exists(socrata_file):
    existing_metadata = pd.read_csv(socrata_file)
    processed_pages = set(existing_metadata['landing_page'])
else:
    existing_metadata = pd.DataFrame()
    processed_pages = set()

#2. filter input dataframe
rows_to_check = df_lp_socrata_pd[~df_lp_socrata_pd['landing_page'].isin(processed_pages)]

print(f'Already processed {len(processed_pages)} pages.')
print(f'Processing {len(rows_to_check)} pages.')

#3. define metadata extraction function
def get_socrata_data(landing_page_url):
    '''
    Uses the landing page URL to check if it matches the Socrata pattern.
    If it does, the function will then obtain the relevant data information.
    '''
    pattern = r'https://([\w\.-]+)/(?:resource|d|views)/([\w\-]+)(?:\.json)?'
    match = re.search(pattern, landing_page_url)
    if not match:
        return {
            'supported_socrata':0,
            'domain': None,
            'dataset_id': None,
            'row_count': None,
            'columns': None
        }
    domain, dataset_id = match.groups()
    metadata_url = f'https://{domain}/api/views/{dataset_id}.json'

    try:
        response = requests.get(metadata_url, timeout=10)
        response.raise_for_status()
        metadata = response.json()

        row_count = metadata.get('rowsUpdatedCount', None)
        columns_info = [
            {'name': col['name'], 'type':col['dataTypeName'], 'description': col['description']}
            for col in metadata.get('columns', [])
        ]

        return {
            'supported_socrata': 1,
            'domain': domain,
            'dataset_id': dataset_id,
            'row_count': row_count,
            'columns': columns_info
        }
    except Exception as e:
        return {
            'supported_socrata': 0,
            'domain': domain,
            'dataset_id': dataset_id,
            'row_count': None,
            'columns': None
        }

def extract_metadata(row):
    metadata = get_socrata_data(row['landing_page'])
    metadata['landing_page'] = row['landing_page']
    metadata['name'] = row['name']
    metadata['id'] = row['id']
    return metadata

#4. batch process and save periodically
batch_size = 250
temp_results = []

for index, (_, row) in enumerate(rows_to_check.iterrows()):
    metadata = extract_metadata(row)
    temp_results.append(metadata)

    #save every N rows
    if (index + 1) % batch_size == 0 or (index + 1) == len(rows_to_check):
        #print(f'Saving progress at {index + 1} processed datasets.')
        new_metadata = pd.DataFrame(temp_results)

        #concatenate datasets
        updated_metadata = pd.concat([existing_metadata, new_metadata], ignore_index=True)

        #save updates
        updated_metadata.to_csv(socrata_file, index=False)

        #reset temp file
        existing_metadata = updated_metadata
        processed_pages.update(new_metadata['landing_page'])
        print(f'{(len(processed_pages)) / (len(rows_to_check) + len(processed_pages)):.2%} complete.')
        temp_results = []

socrata_test = pd.read_csv(socrata_file)

#split supported socrata vs nonsupported socrata
socrata_df = socrata_test[socrata_test['supported_socrata'] == 1]
socrata_unsup = socrata_test[socrata_test['supported_socrata'] == 0]

count_empty = socrata_df['columns'].apply(lambda x: len(x) == 0).sum()

#count empty columns
empty_col = socrata_df['columns'].apply(lambda x: isinstance(x, list) and len(x) == 0).sum()

print(empty_col)

print(type(socrata_df['columns']))

empties = 0
non_empties = 0
for index, row in socrata_df.iterrows():
    if row['columns'] == '[]':
        empties += 1
    else:
        non_empties += 1

#filter empty 'columns'
empties = socrata_df[socrata_df['columns'] == '[]']

#filter nonempty 'columns
non_empties = socrata_df[socrata_df['columns'] != '[]']

non_empties

#merge dataframes
df2 = spark.createDataFrame(non_empties)

#merge dataframes
merged = df.join(df2, 'id', 'inner')

print(merged.count())

merged_df = merged.toPandas()

merged_df.to_csv('/dbfs/user/hive/warehouse/merged.csv', index=False)

#read file into spark dataframe
merged_frame = spark.read.format('csv').load('/FileStore/merged_df.csv')

merged.columns = merged.iloc[0]
merged = merged[1:]

merged = pd.read_csv('/dbfs/FileStore/merged_table.csv')

display(merged)

print(len(empties))

print(len(non_empties))

display(empties)

print(empties)

print(non_empties + empties)

print(type(socrata_df['columns'].iloc[2]))

socrata_df

display(socrata_df)

print(len(socrata_df))

print(len(socrata_unsup))

spark_df = spark.createDataFrame(socrata_df)

display(spark_df)
