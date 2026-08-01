# AQI vs Public Health Search Interest

## The Question
Does national air quality (AQI) in India predict a rise in public search interest 
for respiratory health terms — like "cough," "breathing problem," and "asthma" — 
in the same month or with a delay?

## Why This Matters
Understanding how air pollution connects to public health-seeking behavior could 
help time public health awareness campaigns and identify which symptoms the public 
associates with poor air quality.

## Data Sources
- **Air Quality Index:** "Air Quality Data in India (2015-2020)" (Kaggle), daily 
  readings across 26 Indian cities, aggregated to monthly national averages
- **Search Interest:** Google Trends, monthly search volume (India-wide) for 
  "cough," "breathing problem," and "asthma," Dec 2014 - May 2020

## Method
1. Loaded and stored AQI data in a SQL database (SQLite), cleaned missing values
2. Aggregated daily, per-city AQI into monthly national averages using Python/pandas
3. Merged with Google Trends monthly search data by month
4. Computed correlation between AQI and each search term at same-month, 1-month, 
   2-month, and 3-month lags
5. Built an interactive Power BI dashboard to visualize the relationship

## Key Finding
Cough search interest tracks AQI most strongly in the same month (r=0.35), 
weakening and reversing at longer lags — likely reflecting AQI's own seasonal 
cycle (winter highs, summer lows) rather than a true delayed effect. Asthma 
search interest showed a more gradual, stable relationship, staying mildly 
positive through a 2-month lag (r≈0.20-0.22), suggesting acute symptoms like 
coughing track pollution immediately, while asthma-related searches may build 
up more gradually.

## Dashboard
![Dashboard screenshot](dashboard/screenshot.png)

## Tools Used
SQL (SQLite), Python (pandas), Power BI

## What I'd Do Next
Break this down by city instead of national average, and add hospital admission 
data to check whether search interest actually predicts real health outcomes, 
not just search behavior.