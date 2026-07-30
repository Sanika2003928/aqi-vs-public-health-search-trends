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