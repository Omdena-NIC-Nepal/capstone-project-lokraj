import streamlit as st

def show_about_glacier():
    st.title(" About Glacier Monitoring Module")

    st.markdown("""
This module analyzes glacial retreat using historical glacier imagery, weather station data, and ERA5 climate reanalysis datasets.

**Key Steps:**
- Extracted glacier area over time
- Modeled glacier retreat with climate variables (t2m, tp, sf)
- Forecasted glacier shrinkage till 2050
- Built using Machine Learning Regression Models

**Datasets Used:**
- NASA EarthData Glacier Images
- WMO Weather Station Data
- ERA5 Climate Reanalysis (ECMWF)

**Goal:**
- Understand climate-driven glacier melt in Nepal
- Provide policymakers with future glacier health forecasts
""")
