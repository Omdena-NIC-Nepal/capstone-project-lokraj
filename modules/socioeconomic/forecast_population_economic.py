
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_population_forecast():
    st.subheader(" Forecast: Nepal Total Population (Census Intervals)")
    
    # Load real forecast data
    try:
        df_forecast = pd.read_csv("data/Socioeconomic/clean_data/forecast_population.csv")
        st.dataframe(df_forecast.set_index("Forecast Year"), use_container_width=True)

        # Plot
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(df_forecast["Forecast Year"], df_forecast["Predicted Population"], marker='o', linestyle='--', color='green')
        ax.set_title("Forecasted Population Growth (Census Years)")
        ax.set_ylabel("Population")
        ax.grid(True)
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Failed to load population forecast: {e}")

def show_economic_loss_forecast():
    st.subheader(" Forecast: Land Affected by Climate Disasters (ha)")

    # Load real forecast data
    try:
        df_forecast = pd.read_csv("data/Socioeconomic/clean_data/forecast_economic_loss.csv")
        st.dataframe(df_forecast.set_index("Forecast Year"), use_container_width=True)

        # Plot
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(df_forecast["Forecast Year"], df_forecast["Predicted Affected Area (ha)"], marker='o', linestyle='--', color='red')
        ax.set_title("Forecasted Land Degradation (Flood/Erosion Impact)")
        ax.set_ylabel("Affected Area (ha)")
        ax.grid(True)
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Failed to load economic loss forecast: {e}")

def show_forecast_summary():
    st.markdown("### Population and Economic Loss Forecasts")
    show_population_forecast()
    st.markdown("---")
    show_economic_loss_forecast()
