import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show_water_health():
    st.title(" River Discharge Trends in Nepal")

    df = pd.read_csv("data/Environmental/processed_combined/land_forest_river_glacial_combined_features.csv")

    st.subheader("River Discharge Dataset Overview")
    st.dataframe(df[["Year", "Mean_Discharge_m3s"]])

    st.subheader(" Mean River Discharge Over Time")
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=df, x="Year", y="Mean_Discharge_m3s")
    plt.title("Yearly Mean River Discharge (m³/s)")
    plt.xlabel("Year")
    plt.ylabel("Mean Discharge (m³/s)")
    plt.grid(True)
    st.pyplot(plt.gcf())
