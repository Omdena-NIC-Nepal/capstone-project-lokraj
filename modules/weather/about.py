import streamlit as st

def show_about():
    st.title("📖 About the Nepal Climate and Development Dashboard")

    st.markdown("""
# 🌍 Project Overview
The **Nepal Climate and Development Dashboard** is an interactive application that enables monitoring, analysis, and visualization of climate change impacts, environmental indicators, and socioeconomic development across Nepal.

It serves as a multi-domain decision-support system, combining:
- 🌦️ Weather and Climate Data
- 🌱 Environmental Health Metrics
- 🏛️ Socioeconomic Development Trends

---

# 🏗️ Project Structure
                

---

# ⚙️ Technologies Used

- Python 3.10+
- Streamlit (Interactive UI)
- Pandas (Data Manipulation)
- Plotly (Interactive Charts)
- Matplotlib (Static Plots)
- PyMannKendall (Trend Analysis)
- Scikit-learn (Scaling, Preprocessing)
- GeoPandas & Folium (Spatial Mapping)
- RapidFuzz (Fuzzy Station Name Matching)

---

# 🛠️ Step-by-Step Data Preparation and Workflow

## 1. Load and Tidy Weather Data
- Used **pandas** to load historical weather CSV files.
- Melted wide-format data into **long-format** for flexible analysis.
- Cleaned column names: removed extra spaces, normalized casing.
- Extracted numeric values from mixed strings like `"21.6/19"`.
- Converted extracted `Value` columns into proper float types.

## 2. Handle Missing Values
- Standardized missing data: replaced `'-'`, `'NA'`, `'N/A'`, and empty cells with `np.nan`.
- Applied **mean imputation** for missing values grouped by parameter.
- Special handling for important parameters like **Total Precipitation (mm)** to ensure integrity.

## 3. Normalize Values
- Scaled numerical columns to `[0, 1]` range using `MinMaxScaler`.
- Performed normalization by **station group** or **parameter type** depending on analysis context.

## 4. Temporal Alignment
- Created a **full monthly timeline** grid for every station (Station × Month × Year).
- Merged original data onto this master grid to ensure **uniform monthly time-series**.
- Applied **forward-fill** and **backward-fill** within stations to maintain temporal continuity.

## 5. Georeferencing Stations
- Standardized station names: lowercased and stripped white spaces.
- **Fuzzy matched** station names to GeoJSON municipal boundaries using **RapidFuzz** matching.
- Computed **centroid latitude/longitude** from matched municipalities.

## 6. Spatial Join and Merging
- Aggregated weather parameters (monthly mean, sum) per station.
- Merged with **municipality GeoDataFrames**.
- Preserved **geometry column** for accurate spatial plotting and choropleth mapping.

## 7. Plotting & Mapping
- Created interactive thematic maps using **GeoPandas.explore()** and **Folium**:
  - % of Normal Precipitation
  - Average Monthly Temperature
  - Extreme Rainfall Incidence
- Applied consistent **colormaps**:
  - `YlGnBu` for precipitation
  - `OrRd` for temperature
  - `PuBu` for extreme rainfall

## 8. Export Final Processed Dataset
- Final cleaned dataset exported as:
  - `temporally_aligned_weather_data.csv`
  - Geo-referenced `temporally_aligned_weather_data.geojson`
- Dataset includes fields like:
  - Station Name
  - Date
  - % of Normal Precipitation
  - 24h Extreme Rainfall
  - Matched Latitude/Longitude

---

# 📊 How the Dashboard Navigation Works

1. **Select a Domain**:
    - 🌦️ Climate/Weather
    - 🌱 Environment
    - 🏛️ Socioeconomic Development

2. **Select a Report**:
    - Yearly Trends
    - District Maps
    - Statistical Tests (Mann-Kendall)
    - Sen's Slope Regression
    - About and Documentation

3. **Interact with Visualizations**:
    - Dynamic charts, maps, sliders, and filters.

✅ **Each module is completely independent and modular**, ready for future expansion.

---

# 📈 Expansion Plan

This system is designed to allow:
- Addition of new domains (Disaster Risk, Infrastructure, Health)


---

# 🙏 Acknowledgments

- **Data Sources**:
  - opendatanepal

- **Platform Inspiration**:
  - Omdena Nepal Chapter Collaboration

---



---
    """)

