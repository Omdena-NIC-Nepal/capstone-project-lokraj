import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show_forest_loss_trend():
    st.title(" Forest Area and Forest Loss Trends in Nepal")

    df = pd.read_csv("data/Environmental/processed_combined/land_forest_river_glacial_combined_features.csv")

    st.subheader("Forest Dataset Overview")
    st.dataframe(df[["Year", "Forest_Area_LandCover_km2", "Forest_Loss_ha"]])

    st.subheader(" Forest Area Over Years")
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=df, x="Year", y="Forest_Area_LandCover_km2")
    plt.title("Yearly Forest Area (km²)")
    plt.xlabel("Year")
    plt.ylabel("Forest Area (km²)")
    plt.grid(True)
    st.pyplot(plt.gcf())

    st.subheader(" Forest Loss Over Years")
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=df, x="Year", y="Forest_Loss_ha")
    plt.title("Yearly Forest Loss (hectares)")
    plt.xlabel("Year")
    plt.ylabel("Forest Loss (ha)")
    plt.grid(True)
    st.pyplot(plt.gcf())
