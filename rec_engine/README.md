# Recommendation Engine Project
[Notebook #1](https://github.com/liv4data/projects/blob/06730fc52d9641ccd19e4bb2e8afd5fc57729c7a/rec_engine/recengine1.py) -- this is a .py file\
[Notebook #2](https://github.com/liv4data/projects/blob/25b0befb7a0600c029bc9dce36bce352cc6bf3d2/rec_engine/recengine2.py) -- this is a .py file\
[Notebook #3](https://nbviewer.org/github/liv4data/projects/blob/9fa91e2e0d9346ed9f1566156f716ad598c5fc62/rec_engine/RecEngine3.ipynb)\
[Notebook #4](https://nbviewer.org/github/liv4data/projects/blob/a24a2a8c74af41ebca7b61b74a3378967ba16e24/RecEngine4.ipynb)

## Background
Many data analytics students use the same projects over and over:
- Predicting survival of Titanic passengers
- Classifying wines
- Creating a recommendation engine from the MovieLens dataset

While public data sources like Kaggle and Hugging Face can be great for students aiming to learn various data analysis techniques, they largely ignore the largest steps of a data project: collection and cleaning. As cleverly stated by Mitch Kapor, there is an overwhelming amount of information on the internet, and it can be difficult for students to decide how to start a project.

> Getting information off the internet is like taking a drink from a fire hydrant.
-- Mitch Kapor

## Goal and Tasks
Goal: Develop a recommendation engine that suggests best datasets to match a knowledge domain and project type for data science students.

Major Tasks:
- Compile a set of public datasets
- Use NLP to gleam insights about dataset domain (topic)
- Identify project types and domains for user selection
- Create vector embeddings of datasets and map to project and domain choices

## Approach
### Pipeline
![Image depcting the pipeline of the dataset project recommendation engine from source to output.](https://github.com/liv4data/projects/blob/571f927f5059d684b680ee5c8f42e8c9465262ff/rec_engine/data_pipeline.png)

### Ingestion
Metadata of public datasets was retrieved from data.gov using the CKAN API into a parquet file using Databricks and pyspark. The metadata retrieved with the CKAN API included the title, ID, name, date metadata last modified, description, date published, date modified, landing page, access level, organization, group, tags, resources, and formats. 

Of the 310,512 datasets listed on data.gov, 201,699 were considered private, or had some level of restriction. This includes datasets that are inherently “public” but must be requested in order to access. Of the no-restriction open datasets, 53,945 did not have a landing page and were excluded. To reduce the number of requests and avoid hitting the throttling limit, each dataset’s landing page was compared to the typical Socrata pattern, excluding an additional 39,936 datasets. This left a remainder of 14,942 datasets to retrieve metadata using the Socrata API (SODA).  

For each dataset, if the landing page matched a Socrata JSON object, it would retrieve the domain, dataset ID, and features (columns) for the dataset. This led to a final dataframe of 8,473 public datasets. 

### Preprocessing & Storage
Using Databricks, the initial set of public datasets were saved to a parquet file. The dataframe of the 8,473 datasets Socrata metadata was merged with the IDs of the metadata retrieved using the CKAN API and saved to a CSV file. 

Knowledge domains for the datasets were defined using a three-level hierarchy of domain > topic > subtopic. I custom defined these using common terminology from Wikipedia and Google. A pandas dataframe was created for the topic mapping and the three-level hierarchy was concatenated into a single column.

For each dataset, the features were contained in a list of nested dictionaries. A set was created to collect the feature types across all datasets. Counts of features were added to the dataframe, with one column for the total number of features per dataset, and one column for each feature type. 

The project choices were defined by identifying potential projects that could be used with each feature/data type present in the set feature_types. Using a simple counting function, I scored the suitability of each project for each dataset. Upon viewing the scoring distributions, I noted that a majority of the projects needed refined heuristics. The projects were then rescored for each dataset, and normalized using z-score. 

A dataframe was created using the ID, title, tags, description, feature names, and feature descriptions for each dataset. The five string columns were concatenated, then simple string processing and BeautifulSoup removed extra symbols, HTML formatting, and URLs present in the text. 

### Embedding Generation
Vector embeddings were generated with SentenceTransformer and the model ‘all-MiniLM-L6-v2’. A vector embedding was created for the concatenated column in the topic_choices dataframe. A second vector embedding was created for the concatenated string column in the dataframe of dataset topics. 

### Vector Storage
A final dataframe for the datasets was created by merging together the project scoring, the dataset topics, and some columns of the initial dataframe read in from the CSV file. This final dataframe included the ID from CKAN, the Socrata ID, a score for each project, title, description, tags, feature names, feature descriptions, the vector embedding for the concatenated context of each dataset, organization that posted the dataset, and the landing page. 

Both the dataset_recommender dataframe and topic_choices dataframe with their embeddings were uploaded to Qdrant. For these two collections, the cosine similarity was specified for the distance measure. 

### Recommender Interface
The notebook displays the 6 potential knowledge domains to the user for selection, and then possible topic options for the chosen domain. The user is then able to select one of the eight project types. The domain and topic are located in the topic_choices dataframe, and its embedding is used to query Qdrant for the 10 closest datasets, ranked by project suitability. The matches are then presented to the user with its title, description and landing page URL. 

![Image depicting the flowchart of the dataset project recommendation engine.](https://github.com/liv4data/projects/blob/a8d71f82b50385c20bb9769b43d60fa4b387c4e3/rec_engine/Data_Flow.png)
