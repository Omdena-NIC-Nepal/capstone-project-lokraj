import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_historical_trend():
    st.header(" Historical Glacier Area Trends")

    # Load glacier area history
    glacier_df = pd.read_csv("data/glacier/glacier_area_trend.csv")

    # Plot
    plt.figure(figsize=(10,6))
    plt.plot(pd.to_datetime(glacier_df['date']), glacier_df['glacier_area_percent'], 'bo-', label="Observed Glacier Area (%)")
    plt.title("Historical Glacier Area Changes")
    plt.xlabel("Year")
    plt.ylabel("Glacier Area Percent")
    plt.grid(True)
    plt.legend()
    st.pyplot(plt)
