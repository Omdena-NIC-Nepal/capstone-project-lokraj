import streamlit as st
import pandas as pd
import plotly.express as px
from dateutil import parser

def show_trend_chart_weather():
    st.title("📈 Yearly Extreme Event Trends")
    st.subheader("📊 Explore climate extremes across Nepal over time.")

    try:
        df = pd.read_csv('data/Weather_&_Climate/district_wise/processed_climate_data_nepal.csv')
        st.success("✅ Climate data loaded.")
        st.write(df.head())
    except Exception as e:
        st.error("❌ Failed to load climate data.")
        st.exception(e)
        return

    try:
        df['date'] = pd.to_datetime(df['date'], format='mixed')
    except Exception:
        df['date'] = df['date'].apply(lambda x: parser.parse(x) if pd.notnull(x) else pd.NaT)

    df = df.dropna(subset=['date'])
    df['year'] = df['date'].dt.year

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

    summary = df.groupby(['year', 'event_type']).size().reset_index(name='count')

    if summary.empty:
        st.warning("⚠️ No extreme events found.")
        return

    fig = px.bar(summary, x='year', y='count', color='event_type',
                 title='Extreme Weather Events by Type Over Years',
                 labels={'count': 'Number of Events', 'year': 'Year', 'event_type': 'Event Type'},
                 barmode='stack')

    st.plotly_chart(fig, use_container_width=True)
