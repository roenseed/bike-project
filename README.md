# **CASE STUDY: CYCLISTIC BIKE-SHARE DATA ANALYSIS PROJECT**

![AI Photo](./Image/ai_gen.webp)

**The Case Study from Google Data Analytics Professional Certificate: Cyclistic Bike Share Analysis for Marketing Purposes**

## ABOUT THE COMPANY
Cyclistic launched a bike-share program in 2016, growing to a fleet of 5,824 tracked bikes across 692 stations in Chicago. The bikes can be unlocked from one station and returned to any other. Cyclistic offers flexible pricing plans: single-ride passes, full-day passes, and annual memberships. Casual riders purchase single-ride or full-day passes, while annual memberships are for Cyclistic members.  

Financial analysts have found that annual members are more profitable than casual riders. Despite the pricing flexibility attracting more customers, the goal is to increase the number of annual members for future growth. Moreno, the Director of Marketing, believes converting casual riders into members is a viable strategy since they are already familiar with Cyclistic.  

The marketing team needs to understand the differences between casual riders and annual members, why casual riders might buy a membership, and how digital media could influence marketing tactics. They aim to analyze historical bike trip data to identify trends and design targeted marketing strategies.

## SCENARIO

![AI Photo](./Image/ai_gen_2.webp)

#### MARKETING TEAM
As a junior data analyst in Cyclistic's Marketing Analysis Team, your goal is to understand the different usage patterns between casual riders and annual members. The Director of Marketing believes increasing annual memberships is key to Cyclistic's success. Your team will use these insights to design a marketing strategy aimed at converting casual riders into annual members. To gain executive approval, your recommendations must be supported by compelling data insights and professional visualizations.

## KEY STAKEHOLDERS

> 1. **Lily Moreno:** The director of marketing and my manager. Moreno is responsible for the development of campaigns and initiatives to promote the bike-share program. 
> 2. **Cyclistic marketing analytics team:** A team of data analysts who are responsible for collecting, analyzing, and reporting data that helps guide Cyclistic marketing strategy. 
> 3. **Cyclistic executive team:** A notoriously detail-oriented team that will decide whether to approve the recommended marketing program.

## KEY BUSINESS TASKS
> 1. How do annual members and casual riders use Cyclistic bikes differently?
> 2. Why would casual riders buy Cyclistic annual memberships?
> 3. How can Cyclistic use digital media to influence casual riders to become members?

## KEY BUSINESS OBJECTIVES
1. **Understand Key Insights**: Gain a comprehensive understanding of bike riders' preferences, differentiate between member and casual riders, and analyze the specific needs of each user type for different bike models.
2. **Leverage Growth Profits**: Utilize the insights from financial analysts who emphasize that increasing the number of annual members will significantly boost profitability.
3. **Critical Marketing Influence Timing**: Identify the optimal times for marketing efforts to effectively influence casual riders to consider annual memberships and to maximize growth in membership numbers.
4. **Data-Driven Decision Making**: Use key insights from data analysis to secure executive approval for a marketing plan and strategy. Ensure that recommendations are actionable and profitable, backed by thorough database insights.

## PROJECT STRUCTURE
1. **Data Collection**: Gathering historical bike trip data from Cyclistic's database.
2. **Data Cleaning**: Ensuring data accuracy and completeness by handling missing values, duplicates, and inconsistencies.
3. **Data Analysis**: Performing exploratory data analysis (EDA) to identify trends and patterns in bike usage among casual riders and annual members.
4. **Visualization**: Creating professional visualizations to effectively communicate findings to stakeholders.
5. **Recommendation**: Formulating actionable marketing strategies based on data insights to convert casual riders into annual members.
6. **Presentation**: Preparing a comprehensive presentation to secure executive approval for the proposed marketing strategy.

## KEY DATA PROCESSING AND ANALYSIS
### **Data Collection** 
- The public data has been made available by Motivate International Inc. under license: [(Data License Agreement | Divvy Bikes)](https://divvybikes.com/data-license-agreement)
- The downloaded original dataset from Cyclistic is reliable, accurate, and comprehensive records with complete and unbiased information and it is proven fit for use.
- To access the original public dataset source from [(divvy-tripdata)](https://divvy-tripdata.s3.amazonaws.com/index.html)

### **Data Cleaning and Modeling** 
- The preliminary data cleaning step begins with load 12 .csv, each csv represents a one-month dataset of the year 2022, datasets into the Jupyter Notebook with Python3 (ipykernal).
- The Data Cleaning ensures data accuracy and completeness by handling missing values, duplicates, and inconsistencies
- Here is my essential data cleaning and modeling process through [Python Script](https://github.com/roenseed/bike-project/blob/main/bike_clean.ipynb)

#### **Example Detailed Steps:**
1. **Loading Data:**
   - Import necessary libraries (`pandas`, `os`, etc.).
   - Load the CSV files into dataframes.
   ```python
   import pandas as pd
   import os

   # Load each month's data
   jan_data = pd.read_csv('202201-divvy-tripdata.csv')
   feb_data = pd.read_csv('202202-divvy-tripdata.csv')
   # Continue for all months...

## SIGNIFICANT TOOLS
- **Python**: For data cleaning, analysis, and visualization.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib and Seaborn**: For creating visualizations.
- **SQL**: For querying Cyclistic's database.
- **Power BI/Tableau**: For creating dashboards and interactive visualizations.

## EXPECTED OUTCOMES
- A detailed understanding of the differences between casual riders and annual members.
- Identification of key factors that influence casual riders to become annual members.
- Data-driven marketing strategies to increase the number of annual memberships.
- Professional visualizations and a comprehensive presentation to support the proposed marketing strategies.

## CONTRIBUTOR
- **[CHAROEN KASETRUENGPHOL]**: A Data Analyst, responsible for data collection, cleaning, analysis, visualization, and presenting findings.

---

This project is part of the Google Data Analytics Professional Certificate and aims to provide practical experience in data analysis, visualization, and strategic decision-making based on data insights.
