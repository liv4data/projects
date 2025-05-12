# mph-practicum
This repository contains files and text related to my community practicum project. 
## Background
As a Master of Public Health candidate, I was required to complete a community practicum project with a minimum of 200 contact hours on the project. I completed my practicum at the Foodbank of Southeastern Virginia and the Eastern Shore (Foodbank or FSEVA), as I was drawn to their focus on food equity and their core values of people, quality, integrity, stewardship, and collaboration. Through their assistance programs, they operate to distribute foods to clients, and obtain food through purchases, donations, or commodities provided by the United States Department of Agriculture (USDA). 

During the course of my practicum project, I worked alongside the Foodbank's Registered Dietitian to pilot a nutrition initiative called Supporting Wellness at Pantries (SWAP). The purpose of this initiative was to share basic nutrition information about food choices using a stoplight approach. In other words, green means the most healthy options, yellow indicates less healthful options, and red indicates options that were not as healthful. It was important to ensure that with this program, the language and training for partner pantries emphasized that foods weren't inherently "bad," but some were more healthful than others. 

## Project Goals
**Overall goal:** Lay the foundation for the Supporting Wellness at Pantries (SWAP) program
1. Rank Foodbank-purchased foods
2. Develop materials to educate partner agencies about SWAP and how to implement it
3. Establish next steps for sustainability

**Specific Aims:**
1. Analyze proportions of each SWAP rank for food pantries
2. Provide a report-card-like document of analysis to each pantry
3. Develop materials pantries can use for understanding and implementing SWAP 

## Research Paper
Within the context of the practicum project, I analyzed pantries that commonly rely on reseources purchased by or donated to the Foodbank and how much of their distributions are foods that contribute to adverse health outcomes (or "red" foods). Individuals who are food insecure often rely on items received from food banks and food pantries, and the prevalence of chronic health conditions is frequent in these individuals. The overall purpose of this research was to examine if the food pantries were providing better food choices to their clients. 

## Project Hypotheses
**Null Hypothesis:** The proportion of red foods prior to beginning the nutritional conversations with pantries is *equal to* the proportion of red foods after initiating nutritional conversations with pantries. 

  H<sub>0</sub>: p<sub>1,med</sub> = p<sub>2,med</sub>

**Alternate Hypothesis:** The proportion of red foods prior to beginning the nutritional conversations with pantries is *greater than* the proportion of red foods after initiating nutritional conversations with pantries.

  H<sub>a</sub>: p<sub>1,med</sub> > p<sub>2,med</sub>

## Methods
1. Identified and ranked purchased products based on saturated fat, sodium, and sugar content
   
2. Stratified pantries by county and randomy sampled within strata using random number generator
   - Ratio approximately 1 pantry identified represented approximately 5 pantries
         
3. Invoices examined
   - Excluded donated items, as they are often assorted and not ranked
   - CFAP, TANF, TEFAP products excluded, as they are allocated by grant funding

4. Extracted data from database
   - Used Jet Reports add-on in Microsoft Excel, as user permissions were extremely limited
   - Meshed invoice table data with inventory card item
   - Period 1: August 1, 2020 to October 31, 2020
   - Period 2: January 1, 2021 to March 31, 2021
  
5. Created PivotTable of foods, summarizing food rankings by proportion of total extended gross weight
   
6. Tested hypotheses using match-paired test via Paired Wilcoxon Rank Test
   - Used proportion of red foods for testing
   - Performed hypothesis testing with R

## Results

|![Historgram of proportion of red foods before](https://github.com/liv4data/mph-practicum/blob/667dd374be316f463992795997622f2a524bdb29/results_pantries_before.png)|![Histogram of proportion of red foods after](https://github.com/liv4data/mph-practicum/blob/667dd374be316f463992795997622f2a524bdb29/results_pantries_after.png)|
|---|---|
|**Figure 1.** Histogram of the proportion of red foods prior to beginning nutritional conversations with pantries.|**Figure 2.** Histogram of the proportion of red foods six months after initiating nutritional conversations with pantries.|


|Paired Wilcoxon Rank Test| α=0.05 |
|---|---|
| H<sub>0</sub>: p<sub>1,med</sub> = p<sub>2,med</sub> |  H<sub>a</sub>: p<sub>1,med</sub> > p<sub>2,med</sub> |
| V = 121 | p-value = 0.0174 |

## Discussion of Results
The results of the Paired Wilcoxon Rank test resulted in a p-value less than the significance level of 0.05, so the null hypothesis was rejected. Based on the alternative hypothesis, there was a decrease in the proportion of red foods distributed at the pantries between periods 1 and 2. 

However, it does not necessarily mean that pantries are distributing healthier foods to their clients. When taking into account the amount of grant funding allocated to certain projects as well as the freedom of agencies to select what they would like to receive from the foodbank, each invoice has a different total gross weight of foods distributed. 

### Limitations
1. This study was limited to agencies that made purchases between the two periods and did not include pantries outside of this range, or pantries that received items due to grant funding
   - This excclusion does not necessarily mean that these pantries aren't distributing nutritious foods

2. Due to time constraints, not every food was ranked, which led to exclusions of many items from invoice reports, which could impact the data

## Conclusion
This research led us to understand the nutritional profile of foods distributed by some pantries in the Greater Hampton Roads area. While it does not explain the whole population of food pantries, it does display a potential for improvement as a continuation of the SWAP initiative. Even if a pantry does not want to, or does not have the means to, implement SWAP at their pantry, there are still several methods to change the food pantry landscape and what foods are offered.
