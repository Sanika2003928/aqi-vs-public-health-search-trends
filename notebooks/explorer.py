import pandas as pd

# Load the data
aqi = pd.read_csv("data/raw/city_day.csv")
# Look at the basics
print(aqi.head())
print(aqi.shape)
# Keep only the columns we actually need
aqi_clean = aqi[["City", "Date", "AQI"]]

# Drop rows where AQI is missing — can't analyze what isn't there
aqi_clean = aqi_clean.dropna(subset=["AQI"])

print(aqi_clean.shape)
print(aqi_clean.head())
aqi_clean.to_csv("data/processed/aqi_clean.csv", index=False)
print("Saved!")
trends_cough = pd.read_csv("data/raw/trends_cough.csv")
trends_breathing = pd.read_csv("data/raw/trends_breathing.csv")
trends_asthma = pd.read_csv("data/raw/trends_asthma.csv")

trends = trends_cough.merge(trends_breathing, on="Time").merge(trends_asthma, on="Time")
print(trends.head())
print(trends.shape)
aqi_clean["Date"] = pd.to_datetime(aqi_clean["Date"])
aqi_clean["Month"] = aqi_clean["Date"].dt.to_period("M").dt.to_timestamp()

aqi_monthly = aqi_clean.groupby("Month")["AQI"].mean().reset_index()
print(aqi_monthly.head())
print(aqi_monthly.shape)
# Make sure both date columns match in type and name
trends["Time"] = pd.to_datetime(trends["Time"])
aqi_monthly = aqi_monthly.rename(columns={"Month": "Time"})

# Merge AQI and search trends by month
combined = aqi_monthly.merge(trends, on="Time")
print(combined.shape)
print(combined.head())

# Same-month correlation
print("Same month correlation:")
print(combined[["AQI", "cough", "breathing problem", "asthma"]].corr()["AQI"])

# 1-month lag: shift search terms back by 1 month
combined_sorted = combined.sort_values("Time")
combined_sorted["cough_lag1"] = combined_sorted["cough"].shift(-1)
combined_sorted["breathing_lag1"] = combined_sorted["breathing problem"].shift(-1)
combined_sorted["asthma_lag1"] = combined_sorted["asthma"].shift(-1)

print("1-month lag correlation:")
print(combined_sorted[["AQI", "cough_lag1", "breathing_lag1", "asthma_lag1"]].corr()["AQI"])
combined_sorted["cough_lag2"] = combined_sorted["cough"].shift(-2)
combined_sorted["breathing_lag2"] = combined_sorted["breathing problem"].shift(-2)
combined_sorted["asthma_lag2"] = combined_sorted["asthma"].shift(-2)

combined_sorted["cough_lag3"] = combined_sorted["cough"].shift(-3)
combined_sorted["breathing_lag3"] = combined_sorted["breathing problem"].shift(-3)
combined_sorted["asthma_lag3"] = combined_sorted["asthma"].shift(-3)

print("2-month lag correlation:")
print(combined_sorted[["AQI", "cough_lag2", "breathing_lag2", "asthma_lag2"]].corr()["AQI"])

print("3-month lag correlation:")
print(combined_sorted[["AQI", "cough_lag3", "breathing_lag3", "asthma_lag3"]].corr()["AQI"])

# Save the final combined dataset for the dashboard
combined_sorted.to_csv("data/processed/final_combined.csv", index=False)
print("Final data saved for dashboard!")