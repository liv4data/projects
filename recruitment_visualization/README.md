# Recruitment Visualizations
## Background
Clinical research trials are only as successful as the validity of the data allows. When it comes to clinical trials, data is collected in individual participants, depending on the nature of the condition or investigational product being studied. It is important that each clinical trial has a carefully tailored approach to recruiting study subjects, as potential subjects hear about studies from a variety of sources. 

## Goal & Tasks
**Goal:** Create a report of clinical trial recruitment data to guide recruitment strategies by study focus for future clinical trials.

**Major Tasks:**
- Clean and aggregate study-level recruitment data
- Identify studies by focus, product, and enrollment goals
- Define key metrics for recruitment
- Curate report of recruitment data

## Approach
### Data Cleaning
Recruitment data is maintained in several separate spreadsheets for each individual trial. The five major spreadsheets are: one master list of previous study participants interested in future studies, one for currently enrolling studies, and one for each of the three major sponsors. In these “leads trackers”, potential subjects are listed with their date of birth, contact information, recruiting source, date of contact, date of in-clinic screening appointment, status within the recruitment funnel, and any notes. 

Duplicate listings within a single tracker were removed, and each lead was coded by both recruitment source and status. Recruiting sources were grouped into nine major categories: central, employee/student, established, local, online, provider, transfer, unknown, or word of mouth. The specific source was kept in a separate column, as it could provide further insight into what recruiting sources are most effective for future studies. 

Potential subjects were then codified based on their status within the recruitment funnel. These status codes were active, discontinued, did not qualify, done, lost to follow up, no longer interested, no show or cancelled appointment, nonresponsive to contact, screened, and screen failed. Within a clinical trial, recruitment and retention are considered separately, so the recruitment leads tracker often had data that was different than the screening and enrollment list for a study.

<img src="https://github.com/liv4data/projects/blob/35980563442fb3340f294533184dcb6592407e93/recruitment_visualization/recruitment_funnel_detailed.png" height=500>

For every study, the screening and enrollment list was checked to ensure individuals in the leads tracker were correctly coded by status. If a screening and enrollment list was not available, the source charts were used to create a list to then code the leads. Other leads within the study were then categorized based on available notes, some resulting with an “unknown” status.

### Aggregation
Once individual leads trackers were cleaned, the data were aggregated into a single spreadsheet. The data points for this spreadsheet were the protocol ID for the study, the cohort (if applicable), source category, detailed source, date of last contact attempt, date of screening appointment, and status. This allowed for the recruitment leads for each study to be de-identified for analysis.

A simple database of previous studies is currently in development. This database includes information related to site conduct of the study such as the protocol ID, the sponsor, the principal investigator, study status, protocol title, nickname, funding and grant number, IRB of record, and IRB number. It also contains important study dates such as IRB approval, site initiation visit, activation, enrollment closure, close-out visit, and IRB termination. It also holds protocol-specific information that can be useful for recruiting reports such as study phase, investigational product type, study focus, associated medical conditions, samples collected, study endpoints, and procedures. While this database is a relatively new effort, studies within this recruitment analysis were of highest priority for entry. The study information was exported from the database to a spreadsheet for analysis.

Both the cleaned recruiting data spreadsheet and study information spreadsheet were connected to Power BI to create the recruiting reports used for analysis. Analysis of the aggregated enrollment lists for each study was calculated using Microsoft Excel.

For the aggregated screening-enrollment list, a Pivot Table was used to generate the number of total screenings per year and the number of studies enrolling per year. These numbers were then used to estimate the average number of screenings per study per year, calculated as the number of screenings divided by the number of studies. These results were then plotted by year.

### Defining Metrics
| Metric | Explanation |
| --- | --- |
| Contact : Screen Ratio | # of individuals contacted for one in-person screening |
| Screen : Enroll Ratio | # of individuals screened for one to enroll |
| SF Rate | % of individuals screened that did not meet eligibility criteria |
| Completion Rate | % of individuals enrolled that completed study |

## Results
<img src="https://github.com/liv4data/projects/blob/35980563442fb3340f294533184dcb6592407e93/recruitment_visualization/recstats_p1.png" width=490> <img src="https://github.com/liv4data/projects/blob/35980563442fb3340f294533184dcb6592407e93/recruitment_visualization/recstats_p2.png" width=490>
<img src="https://github.com/liv4data/projects/blob/35980563442fb3340f294533184dcb6592407e93/recruitment_visualization/recstats_p3.png" width=490> <img src="https://github.com/liv4data/projects/blob/35980563442fb3340f294533184dcb6592407e93/recruitment_visualization/recstats_p4.png" width=490>
<img src="https://github.com/liv4data/projects/blob/35980563442fb3340f294533184dcb6592407e93/recruitment_visualization/recstats_p5.png" width=490> <img src="https://github.com/liv4data/projects/blob/35980563442fb3340f294533184dcb6592407e93/recruitment_visualization/recstats_p6.png" width=490>

## Discussion & Insights
It is worthwhile to keep in mind that while these leads trackers aim to keep detailed notes of interactions with potential study subjects, turnover over the years has made it difficult to develop and communicate a standard to future recruiters. Also, these counts are solely based on the number of individuals contacted per study, and not the number of contact attempts. This is information that is not easily trackable within the same spreadsheet (for someone with minimal Excel knowledge). The general rule is a minimum of three contact attempts must be made prior to categorizing as nonresponsive. So while there may have been a total of 2336 leads tallied as such, several more attempts were made. Even in the case of responsive subjects, there are often multiple contact attempts prior to being able to phone screen the individual.

![](https://github.com/liv4data/projects/blob/b0b66122dfa13cc1d54c4309033df16bc2e58414/recruitment_visualization/Source%20data.png)

As depicted in the table above, the largest proportion of leads came from central recruiting efforts, at 63%. However, this solely accounts for a large number of leads generated by a third-party effort, and does not account for the responsiveness of the potential subjects.

The largest proportion of screened subjects were recruited from central advertisements at 36% and the established subject pool at 26%. However, when looking at screened subjects who enrolled in the study as depicted in the table below, the established subject pool was higher at 32%, while central advertisements sat at 24%.

![](https://github.com/liv4data/projects/blob/208000971d8285a525d907200c676ef2413ea01a/recruitment_visualization/updated%20source%20enrolled.png)

Screening and enrollment lists were available for 49 studies over the last 10 years. These studies encompass a variety of projects, including fertility studies. As depicted below, the peak of total screening visits occurred during the years of 2018 and 2019, with 195 screenings and 225 screenings, respectively. While there was an increase of 25 screenings from 2020 to 2021, it is worthwhile noting the closure in 2020 due to the COVID-10 pandemic. However, since 2021, there has been a significant decrease in total screenings per year, with no new projects anticipated in the latter half of the 2024 calendar year.

![](https://github.com/liv4data/projects/blob/40ff8369c8e08b98f47d38692a2269611817a0d5/recruitment_visualization/Screens%20per%20year.png)

Depicted in the figure below, the average number of screenings per study has steadily decreased over the last 5 years, from an average of 16.3 screens per study in 2018, to an average of 7.9 screens per study in 2023. While the number of enrolling studies has varied over the last 10 years, there has been a steady decrease in the number of enrolling studies since 2021. The number of enrolling studies for 2024 is 7, which is half the number of enrolling studies in 2021 (14).

![](https://github.com/liv4data/projects/blob/c9bd79d6ed2db7d078529a211ed875c18197c5b3/recruitment_visualization/screens%20per%20study%20per%20year.png)

## Limitations
There are a few notable limitations of this analysis of recruitment and screening/enrollment data. First, not all studies were included in the screening-enrollment data. Two major ongoing studies excluded are sample collection studies based out of the hospital, as such it is not fair to include them in this analysis, as they do not require the same recruitment efforts. Also, while only limited studies were included from the years 2014 to 2018, all clinical trials conducted within the last 5 years were included. 

The second major limitation of this analysis lies with the available recruitment data. Only 29 of the 51 studies with recruiting spreadsheets were included. The remaining 43% of these studies had extremely incomplete data, often limited to individuals enrolled in the study, or simply a list of names with no information as to the source or status of the individual. A noteworthy example of this exclusion lies with four menopause studies that were conducted and enrolled between 2018 and 2022. It appeared that the recruitment spreadsheets for three of the studies were copied and pasted from the first study. Further inspection of these trackers revealed that only some of the individuals had updated notes and dates, while others did not have any updated information at all. While it is likely that these individuals were considered for the subsequent menopause studies, it is impossible to determine whether or not the individual was contacted without updated notes.

## Future Suggestions
Moving forward, the site should have a solid recruitment database that is easily able to track recruiting efforts. Not only should it track the study, recruiting source, and final status of the individual, but it should also be able to track the number of contact attempts made to an individual so that accurate budgets can be prepared with respect to recruitment efforts. 

The site is currently piloting the use of a tool free to clinical research sites to manage and track recruiting data. The system is HIPAA and GDPR compliant, as data is secure and encrypted. Potential subjects are added to the database, which is visible only to authorized site users, administered by staff. The potential subject may be linked to one or multiple trials, and the status can be updated accordingly. This allows for the recruiter to quickly determine if the potential subject is available for an enrolling study. The system tracks the recruiting source, number of contact attempts, method of contact, date of contact, and notes entered by the recruiter. The system is collaborative, allowing coordinators to also have access in the event of recruiter absence. The system also allows for text messaging a potential subject, which aids in initial contact, as many individuals no longer answer a call from an unknown phone number. Inclusion and exclusion criteria can be added for each study protocol, for ease of tracking why an individual does not qualify. Deidentified reports can be downloaded and shared with sponsors to provide evidence for recruitment efforts, with attention to inclusion and exclusion criteria.

It might also be beneficial to make the report interactive within Power BI, adding in funcitonality with buttons, additional filters, and visualizations. However, the current staff is not familiar with interactive visualizations or Power BI, so the report would be only helpful as the end user can access. Simply put, ad hoc reports would need to be developed and saved as PDFs. 
