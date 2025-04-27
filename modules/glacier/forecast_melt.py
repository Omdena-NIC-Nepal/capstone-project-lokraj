import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_forecast():
    st.header(" Forecasted Glacier Area Trend till 2050")

    # Load merged dataset and predictions
    merged_df = pd.read_csv("data/glacier/ERA5/merged_glacier_climate_modeling.csv")
    future_df = pd.read_csv("data/glacier/ERA5/future_glacier_forecast.csv") 

    # Plot
    plt.figure(figsize=(12,6))
    plt.plot(merged_df['year'], merged_df['glacier_area_percent'], 'bo-', label="Observed")
    plt.plot(future_df['year'], future_df['predicted_glacier_area_percent'], 'r^-', label="Forecasted")

    plt.title("Forecasted Glacier Area till 2050")
    plt.xlabel("Year")
    plt.ylabel("Glacier Area Percent")
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)
