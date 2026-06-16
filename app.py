import pandas as pd
import streamlit as st

# Load dummy dataset
df = pd.read_csv("dataset/accident_prediction_india.csv1.txt")

st.title("Traffic & Accident Data Analysis Dashboard ")

# Show raw data
st.subheader("Raw Data")
st.dataframe(df)

# Fatalities by State
st.subheader("Total Fatalities by State")
fatalities_by_state = df.groupby("State Name")["Number of Fatalities"].sum()
st.bar_chart(fatalities_by_state)

# Fatalities by Year
st.subheader("Total Fatalities by Year")
fatalities_by_year = df.groupby("Year")["Number of Fatalities"].sum()
st.line_chart(fatalities_by_year)

# Fatalities by Severity
st.subheader("Total Fatalities by Accident Severity")
fatalities_by_severity = df.groupby("Accident Severity")["Number of Fatalities"].sum()
st.bar_chart(fatalities_by_severity)

# Fatalities by Vehicle Type
st.subheader("Total Fatalities by Vehicle Type")
fatalities_by_vehicle = df.groupby("Vehicle Type Involved")["Number of Fatalities"].sum()
st.bar_chart(fatalities_by_vehicle)
