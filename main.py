import pandas as pd

# Load dataset
df = pd.read_csv("dataset/accident_prediction_india.csv1.txt")

# Display first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Total fatalities by state
fatalities_by_state = df.groupby("State Name")["Number of Fatalities"].sum()
print("\n--- Total Fatalities by State ---")
print(fatalities_by_state)

# Total fatalities by year
fatalities_by_year = df.groupby("Year")["Number of Fatalities"].sum()
print("\n--- Total Fatalities by Year ---")
print(fatalities_by_year)
