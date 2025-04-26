import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pymannkendall as mk
import numpy as np
from dateutil import parser

def show_sen_plot():
    st.title("📉 Sen's Slope Trend Plot")

    # Step 1: Load Climate Data
    try:
        df = pd.read_csv('data/Weather_&_Climate/district_wise/processed_climate_data_nepal.csv')
        st.success("✅ Climate data loaded.")
    except Exception as e:
        st.error("❌ Failed to load data.")
        st.exception(e)
        return

    # Step 2: Parse Dates
    try:
        df['date'] = pd.to_datetime(df['date'], format='mixed')
    except Exception:
        df['date'] = df['date'].apply(lambda x: parser.parse(x) if pd.notnull(x) else pd.NaT)

    df = df.dropna(subset=['date'])
    df['year'] = df['date'].dt.year

    # Step 3: Event Classification
    precip_threshold = df['prectot'].quantile(0.95)
    temp_high_threshold = 38
    temp_low_threshold = 0
    wind_speed_threshold = 15

    df['extreme_precip'] = df['prectot'] > precip_threshold
    df['extreme_heat'] = df['t2m_max'] > temp_high_threshold
    df['extreme_cold'] = df['t2m_min'] < temp_low_threshold
    df['extreme_wind'] = df['ws10m_max'] > wind_speed_threshold

    def classify_event(row):
        if row['extreme_precip']:
            return 'Heavy Rain'
        elif row['extreme_heat']:
            return 'Heatwave'
        elif row['extreme_cold']:
            return 'Coldwave'
        elif row['extreme_wind']:
            return 'Windstorm'
        else:
            return 'Normal'

    df['event_type'] = df.apply(classify_event, axis=1)
    df = df[df['event_type'] != 'Normal']

    # Step 4: Dropdown to select event type
    event_types = df['event_type'].unique()
    selected_event = st.selectbox("Select Extreme Event Type:", event_types)

    df_selected = df[df['event_type'] == selected_event]
    yearly_summary = df_selected.groupby('year').size().reset_index(name='count')

    if yearly_summary.empty:
        st.warning("⚠️ No events found for the selected type.")
        return

    # Step 5: Mann-Kendall Test + Sen's Slope
    result = mk.original_test(yearly_summary['count'])

    years = yearly_summary['year'].values
    counts = yearly_summary['count'].values

    slope = result.slope
    intercept = np.median(counts) - slope * np.median(years)
    trend_line = slope * years + intercept

    # Step 6: Plot
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(years, counts, color='blue', label='Observed Events')
    ax.plot(years, trend_line, color='red', linestyle='--', label=f"Sen's Slope ({slope:.2f})")

    ax.set_title(f"Trend in {selected_event} Events Over Years")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Events")
    ax.grid(True)
    ax.legend()

    st.pyplot(fig)

    st.success(f"✅ Mann-Kendall Trend Detected: {result.trend} (p-value={result.p:.4f})")
