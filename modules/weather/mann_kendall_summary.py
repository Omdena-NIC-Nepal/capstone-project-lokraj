import streamlit as st
import pandas as pd
import plotly.express as px
import pymannkendall as mk

def show_mk_results():
    st.title("📐 Mann-Kendall Trend Test Results")

    try:
        df = pd.read_csv('data/Weather_&_Climate/district_wise/processed_climate_data_nepal.csv')
        st.success("✅ Climate data loaded.")
    except Exception as e:
        st.error("❌ Failed to load data.")
        st.exception(e)
        return

    if 'year' not in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
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

    mk_results = []
    for event in summary['event_type'].unique():
        series = summary[summary['event_type'] == event]['count'].values
        if len(series) > 0:
            result = mk.original_test(series)
            mk_results.append({
                'Event Type': event,
                'Sen\'s Slope': result.slope,
                'Significant': 'Yes' if result.p < 0.05 else 'No'
            })

    if not mk_results:
        st.warning("⚠️ No results to display.")
        return

    mk_df = pd.DataFrame(mk_results)
    st.write("📈 Mann-Kendall Summary:", mk_df)

    fig = px.bar(mk_df, x="Event Type", y="Sen's Slope", color="Significant",
                 title="Sen's Slope for Each Extreme Weather Event",
                 labels={"Sen's Slope": "Slope", "Event Type": "Event"},
                 color_discrete_map={"Yes": "green", "No": "red"},
                 text="Sen's Slope")

    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    st.plotly_chart(fig, use_container_width=True)
