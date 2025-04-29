# modules/socioeconomic/economic_loss_forecast.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show_economic_loss_forecast():
    st.subheader(" Land Affected by Climate Disasters (Historical Overview)")

    try:
        # --- Load datasets ---
        df_area = pd.read_csv("data/Socioeconomic/clean_data/economic_loss_area_clean.csv")
        df_disaster = pd.read_csv("data/Socioeconomic/clean_data/economic_loss_disaster_clean.csv")
  
        # --- Part 1: Historical Area Loss by Ecological Belt ---
        st.markdown("###  Land Degradation by Ecological Belt")

        st.dataframe(df_area, use_container_width=True)

        fig1, ax1 = plt.subplots(figsize=(10,6))
        sns.barplot(data=df_area, x="ECOLOGICAL  BELT", y="Affected Area (ha)", ax=ax1, palette="YlOrRd")
        ax1.set_title("Affected Area by Ecological Belt")
        ax1.set_xlabel("Ecological Belt")
        ax1.set_ylabel("Affected Area (ha)")
        st.pyplot(fig1)

        st.markdown("---")

        # --- Part 2: Disaster Impacts Summary ---
        st.markdown("###  Disaster Impacts Summary")

        st.dataframe(df_disaster, use_container_width=True)

        fig2, ax2 = plt.subplots(figsize=(10,6))
        sns.barplot(data=df_disaster, x="Disaster type", y="No. of death", ax=ax2, palette="coolwarm")
        ax2.set_title("Deaths by Disaster Type (1971–2015)")
        ax2.set_xlabel("Disaster Type")
        ax2.set_ylabel("Number of Deaths")
        ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right')
        st.pyplot(fig2)

    except Exception as e:
        st.error(f"Error loading economic loss data: {e}")
