# Semester Project

Olivia Ross  
CS 625, Fall 2025  
Due: Sunday, December 7 by 11:59pm

## Dataset

### National Survey of Family Growth (NSFG)
- [2022-2023 Cycle](https://ftp.cdc.gov/pub/Health_Statistics/NCHS/NSFG/NSFG-2022-2023-FemRespPUFData.zip)
- [2017-2019 Cycle](https://www.cdc.gov/nchs/nsfg/nsfg_2017_2019_puf.htm#downloadable)
- [2015-2017 Cycle](https://www.cdc.gov/nchs/nsfg/nsfg_2015_2017_puf.htm)
- [2013-2015 Cycle](https://www.cdc.gov/nchs/nsfg/nsfg_2013_2015_puf.htm)
- [2011-2013 Cycle](https://www.cdc.gov/nchs/nsfg/nsfg_2011_2013_puf.htm)

[Dataset after EDA/Cleaning](/project/bc-combined-file.csv)

### Notebooks
[Visualization](https://colab.research.google.com/drive/1Er2TUmdCOdbCE4z-YO9UFzutRSewCdCg?usp=sharing)  
[EDA](https://colab.research.google.com/drive/1Ug-m0bUUM7pASErxc9jbRj0idJ3956UU?usp=sharing)

### Final Question

**How has the trend of primary birth control use changed over the last 15 years?**
Answer: Primary birth control use has changed over the last 15 years with an overall decrease in basic hormonal methods (pill, patch, ring, Depo shot), but an increase in long-acting reversible contraception, "LARC", (IUDs and hormonal implants like Nexplanon). Even though this trend is still observed within different religious affiliations, the top primary method used varies between each religious affiliation.


## Image

<img src = "project_final_viz.png" height=500>

### Explanation

By using subplots of four line charts, I was able to show the overall trend of primary birth control methods over time for each religious affiliation (based on the NSFG survey's options - no religion, Catholic, Protestant, or other). Each y-axis is for the proportion of respondents for that specific religious affiliation, which enabled me to compare how the proportions changed from cycle to cycle. The use of a basic categorical color scheme from seaborn enabled me to ensure that there would be no mistaking the categorical nature indicated by the color channel, whereas something like a rainbow may imply some sort of order. 

## Final Thoughts
As with any data project, the part that took the most time was the EDA/cleaning of the data. While investigating each of the individual variables that I was interested in (and realized had some impact on primary birth control method), it was hard to keep myself from making any major visualizations. Once I decided to hone in on the different religious affiliations, I noticed that even though I pared down the options, 8 lines on each chart was still too busy and I realized it took away from the overall message I wanted to convey based on my interesting finding - which was that there was an increase in female sterilization and decrease in basic hormonal methods, as well as several methods having widely different proportions of users by religion. I ultimately decided to focus on the top four methods used nationally, which allowed me to show the overall trends within each subgroup, and gave me additional space to add contextual information about the change in the Affordable Care Act's mandate in 2015, requiring insurance plans to offer at least 1 of the 18 FDA-approved birth control methods to its policyholders with no cost sharing (with some exemptions). In designing my visualization itself, the overall process of the subplots was relatively easy, but the more time-consuming part was formatting everything - particularly when it came to adding the contextual box on the side, the headline, and source info at the bottom.

Overall, I thought this was a very fun assignment, though I am interested in exploring this dataset further. I think there were many factors I didn't fully explore, and I also think it would be interesting to see how the data could be used in more interactive visualizations or dashboards, instead of those that are static. 


## References
Python References:
- https://www.statology.org/pandas-append-two-dataframes/
- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
- https://www.geeksforgeeks.org/pandas/ways-to-filter-pandas-dataframe-by-column-values/
- https://www.statology.org/pandas-groupby-percentage/
- https://python-graph-gallery.com/516-line-chart-with-annotations/
- https://matplotlib.org/stable/gallery/text_labels_and_annotations/annotation_demo.html
- https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html
- https://matplotlib.org/stable/users/explain/text/text_intro.html

National Survey of Family Growth Resources:
*Each page includes both the dataset and codebook that were consulted and used.*
- https://www.cdc.gov/nchs/nsfg/nsfg-2022-2023-puf.htm#female
- https://www.cdc.gov/nchs/nsfg/nsfg_2017_2019_puf.htm
- https://www.cdc.gov/nchs/nsfg/nsfg_2015_2017_puf.htm
- https://www.cdc.gov/nchs/nsfg/nsfg_2013_2015_puf.htm
- https://www.cdc.gov/nchs/nsfg/nsfg_2011_2013_puf.htm

Contraception Resources
- https://www.acog.org/clinical/clinical-guidance/practice-bulletin/articles/2017/11/long-acting-reversible-contraception-implants-and-intrauterine-devices
- https://web.archive.org/web/20150512181805/http://www.nationaljournal.com/health-care/hhs-all-methods-of-birth-control-must-be-covered-20150511
- https://pmc.ncbi.nlm.nih.gov/articles/PMC5576988/

While the 2011-2019 cycles were stored in SAS files, I used the documentation available on the NSFG pages, and the coding was already in the file. Opening the file within SAS created the import, and then I exported the data to a CSV file by following the SAS documentation (https://documentation.sas.com/doc/en/pgmsascdc/v_069/pgmgs/p14twtiyode7jhn18sqqmm68vccf.htm). 
