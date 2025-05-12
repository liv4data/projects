# Cesarean Delivery Classification
[EDA Notebook](https://nbviewer.org/github/liv4data/projects/blob/bc9b6fab55614febb79f8f140c8d4de20d3bd218/natality_classification/natality_EDA.ipynb)\
[Classification Notebook](https://nbviewer.org/github/liv4data/projects/blob/9ad64db0dfeb8e57b914ec30c8f174c37e1cfea7/natality_classification/natality_classification.html)

## Packages & Libraries
- Pyspark (SQL & ML)
- Matplotlib pyplot, Seaborn
- Pandas, Numpy, Scipy, statistics
- itertools, functools

## Introduction
### Background
Healthy People is an initiative that began in 1980 by the US Department of Health and Human Services. Each iteration, released every 10 years, identifies science-based objectives with targets to guide health promotion and disease prevention efforts. The benchmarks established aim to identify priorities for national health improvement, increase public awareness, provide measurable objectives and goals, as well as engaging stakeholders to take action. 

A major objective identified by Healthy People 2030 is MICH-06: reduce cesarean births among low-risk women with now prior births. The baseline for the objective was 2018, in which 25.9% of low-risk females with no prior birth delivered by C-section. In 2022, the rate increased to 26.3%, indicating that the status is getting worse. 

**Why is this important?**\
While C-sections can prevent injury and death in women at higher risk of complicated deliveries and also protect the health of their newborns, C-sections are linked to increased risk of infections and blood clots. Evidence-based strategies can help reduce this risk.

**Who is considered "low-risk"?**\
The methodology used by Healthy People defines women that are low risk are:
- Nulliparous - meaning women who have never given birth. The NVSS makes a distinction that defines parity as how many live births a mother has had.
- Full term - women who are at least 37 weeks pregnant at time of delivery
- Singleton pregnancy - only one baby in utero. Twins or more are considered “multiple”
- Vertex presentation - also known as cephalic, when the head of the baby is pointed downward in the birth canal

## Goal
Develop a machine learning classification algorithm using 2023 natality data to predict whether a mother will deliver vaginally or via C-section.

## Data Source
The CDC’s National Center for Health Statistics (NCHS) [National Vital Statistics System (NVSS)](https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm) provides annual datasets for births, deaths, and datasets linking the two or honing in on certain deaths, such as fetal death or drug overdose. The files directly available on the CDC’s website are large (~4GB) flat files that require input coding. 

As an alternative data source, the [National Bureau of Economic Research (NBER)](https://data.nber.org/nvss/natality/csv/2023/) provides a more user-friendly version of the dataset as a 2GB CSV file with labels added. Since these are posted and available to the public, I was able to read them directly into Spark using Databricks. The runtime took anywhere from 5-30 minutes, depending on the day and time. For this data project, I focused solely on the NVSS data for 2023. 

## EDA Summary
### Basic Observations
The dataset was overall well-organized and documentation provided by NVSS made it easy to familiarize myself with the data. There were 3,605,081 observations in 237 features with 76 of the features considered “reporting flags”. The least reported were age of the mother (based on missing date of birth) and combined gestation (pregnancy estimate based on her last menstrual cycle). There were also features that flagged imputed values, the most were mother’s race at 8%, and combined gestation at 1.5%.

### Initial Observations
When looking at the entire dataset, about two-thirds of the deliveries were vaginal, while about one-third were C-section. When breaking down into specific detail, approximately 96% of vaginal deliveries were not after a previous C-section, and about 3% were after a previous C-section. Of C-section deliveries, 59.6% were a first C-section, and 40% were a repeat C-section. 

For all women who delivered in 2023, about 39% were nulliparous, 31% had one previous delivery, and 29% had at least two previous deliveries. About 94% were cephalic presentation, while about 4% were breech presentation (not head first). Almost 97% were singleton pregnancies. 89.5% of deliveries were full-term, at least 37 weeks. Of the preterm births, about three-fourths were between 34 and 36 weeks.

### Population of Interest
I filtered the dataset for the women meeting the definition of low-risk, which was about one-third of all deliveries for 2023. Of these, about three-fourths (73.4%) delivered vaginally, while one-fourth (26.6%) delivered via C-section. This is an increase from 2022, where 26.3% of low-risk women delivered via C-section. 

I noted the following groups had higher percentages of delivery via C-section:
![Table listing the various characteristics and conditions that had higher percentages of delivery via C-section](https://github.com/liv4data/projects/blob/a761c05057075a0c7d6f7822e094b0b7c70d1cd0/natality_classification/increased_prop.png)

## ML Approach
### Data Prep
The dataset was filtered to only include mothers considered low-risk meeting the previously established definition, and of those with known delivery methods. Any rows containing null or unknown values were removed. 

Smoking was converted to a Boolean value, to be used in two groups: either overall or timing of smoking. One feature maintained the overall Yes/No to smoking, and four features were added that listed Yes/No to smoking during each of the following periods:
- Pre pregnancy
- 1st trimester
- 2nd trimester
- 3rd trimester

### Feature Selection & Engineering
Once the data was prepped, it was split into training and testing datasets, with 80% training and 20% testing. Based on the EDA, downsampling was performed to handle the class imbalance of 74% vaginal deliveries and 26% C-section deliveries. 

Since the data included both continuous values and categorical or ordinal recodes, I created four configurations of the features to compare the predictive power of both, along with the two groups of smoking features. String indexing and one-hot encoding were used in the transformation. 

### Building & Training the Models
I used both logistic regression and random forest models for predicting whether the various factors would lead to a vaginal vs. c-section delivery. All four configurations were used in each model type for a total of eight comparisons. The logistic regression model used 3-fold cross-validation and the random forest models were constructed using 50 trees and then 100 trees. 

## Results
### Logistic Regression
| Config | Config Details | AUC | F1 | Accuracy |
| --- | --- | --- | --- | --- |
| config2 | Categorical recodes and detailed smoking | 0.709007 | 0.672275 | 0.748528 |
| config4 | Categorical recodes and general smoking | 0.709005 | 0.672297 | 0.748575 |
| config1 | Continuous values and detailed smoking | 0.704570 | 0.662541 | 0.745158 |
| config3 | Continuous values and general smoking | 0.7045678 | 0.662436 | 0.745125 |

### Random Forest
| Config | Config Details | AUC | F1 | Accuracy |
| --- | --- | --- | --- | --- |
| config1 | Continuous values and detailed smoking | 0.67771 | 0.62415 | 0.73595 |
| config4 | Categorical recodes and general smoking | 0.67561 | 0.62396 | 0.73587 |
| config3 | Continuous values and general smoking | 0.67393 | 0.62437 | 0.73602 |
| config2 | Categorical recodes and detailed smoking | 0.67205 | 0.62386 | 0.73583 |

## Conclusions & Future Directions
### Strengths
- Large amount of data well-representative of entire population
- Comparison of two models across four sets of features

### Limitations
- Does not account for individual reasoning for elective C-section
- Fair level of accuracy, but needs refining

### Future Diections
- Further explore how the various individual features might be best used within the model (e.g. include vs. exclude certain features)
- Assess differences between recent years
