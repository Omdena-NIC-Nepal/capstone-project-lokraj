import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import json
from dateutil import parser

def show_map():
    st.title("🗺️ District-Wise Extreme Weather Map")

    try:
        df = pd.read_csv('data/Weather_&_Climate/district_wise/processed_climate_data_nepal.csv')
        st.success("✅ Climate data loaded.")
    except Exception as e:
        st.error("❌ Failed to load climate data.")
        st.exception(e)
        return

    try:
        df['date'] = pd.to_datetime(df['date'], format='mixed')
    except Exception:
        df['date'] = df['date'].apply(lambda x: parser.parse(x) if pd.notnull(x) else pd.NaT)

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

    try:
        with open('data/nepal-districts-new.geojson', 'r') as f:
            geo = json.load(f)
        st.success("✅ GeoJSON loaded.")
    except Exception as e:
        st.error("❌ Failed to load GeoJSON.")
        st.exception(e)
        return

    available_years = sorted(df['year'].unique())
    selected_year = st.selectbox("Select Year:", available_years)

    df_year = df[df['year'] == selected_year]
    district_summary = df_year.groupby('district').size().reset_index(name='total_events')

    geo_districts = [feature['properties']['DIST_EN'] for feature in geo['features']]
    event_counts = dict(zip(district_summary['district'], district_summary['total_events']))
    z = [event_counts.get(d, 0) for d in geo_districts]

    fig = go.Figure(go.Choroplethmapbox(
        geojson=geo,
        locations=geo_districts,
        z=z,
        colorscale="Reds",
        marker_line_width=1,
        marker_line_color='black',
        colorbar_title="Event Count",
    ))

    fig.update_layout(
        mapbox_style="carto-positron",
        mapbox_zoom=6.2,
        mapbox_center={"lat": 28.3, "lon": 84.1},
        margin={"r":0,"t":30,"l":0,"b":0}
    )

    st.plotly_chart(fig, use_container_width=True)
