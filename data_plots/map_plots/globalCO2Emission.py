import pandas as pd
import streamlit as st
from plotly import express as px
from utils.enrich_data import get_clean_countries, get_countries

def plot_map_global_co2_emission(data: pd.DataFrame, title: str) -> None:
    st.title(title)
    filtered_data: pd.DataFrame = get_clean_countries(get_countries(data), ['year', 'gdp', 'co2', 'population'])
    selection_year = st.select_slider("Select Year: ", options = [year for year in range(1900, filtered_data['year'].max())])
    map_fig = px.choropleth(
        filtered_data[filtered_data['year'] == selection_year], 
        locations = "iso_code", 
        color = "co2", 
        color_continuous_scale = px.colors.sequential.Plasma, 
        labels = {
            'co2': 'CO2 Emission (in Trillions)', 
            'iso_code': 'ISO Code',
            'country': 'Country',
            'population': 'Population (Million to Billions)',
            'gdp': 'GDP ($)'
        },
        hover_data = [
            "country",
            "population",
            "gdp"
        ],
        # projection="mercator"
    )
    map_fig.update_layout(height = 800, title = "Global CO2 Emission")
    st.plotly_chart(map_fig, use_container_width = True)
    st.write(filtered_data[filtered_data['year'] == selection_year])
    None