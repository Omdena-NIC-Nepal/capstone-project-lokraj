import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show_glacier_formation_trend():
    st.title(" Glacial Lake Area Trends in Nepal")

    df = pd.read_csv("data/Environmental/processed_combined/land_forest_river_glacial_combined_features.csv")

    st.subheader("Glacial Lake Dataset Overview")
    st.dataframe(df[["Year", "Total_Glacial_Lake_Area_km2"]])

    st.subheader(" Total Glacial Lake Area Over Time")
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=df, x="Year", y="Total_Glacial_Lake_Area_km2")
    plt.title("Yearly Total Glacial Lake Area (sq.km)")
    plt.xlabel("Year")
    plt.ylabel("Lake Area (sq.km)")
    plt.grid(True)
    st.pyplot(plt.gcf())
