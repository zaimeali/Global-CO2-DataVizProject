import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from utils.enrich_data import get_countries_filter_remove_empty_column, countries_options

def area_plot_by_region(data: pd.DataFrame) -> None:
    st.header("Area Plot by Region")
    options = {
        "Annual CO2 Emission": "co2",
        "Population": "population"
    }
    selection: str = st.selectbox("Select Column: ", options = options)

    fig = px.area(
        data,
        x = 'year',
        y = options[selection],
        color = "country"
    )
    fig.update_layout(
        title_text = f"Area Plot by Region of {selection} by Year",
        xaxis_title = 'Year',
        yaxis_title = selection.capitalize()
    )
    st.plotly_chart(fig, use_container_width = True)
    None

def area_plot_multi_select_country(data: pd.DataFrame) -> None:
    st.header("Area Plot by Country - (Multi-Select Country) by CO2")
    data = get_countries_filter_remove_empty_column(data, 'co2')
    country_options = countries_options(data)
    selected_countries = st.multiselect("Select Country: ", options = country_options)
    if selected_countries:
        fig = go.Figure()
        for selected_country in selected_countries:
            split = selected_country.split(" - ")
            country_data = data[data['iso_code'] == split[0]]
            fig.add_trace(
                go.Scatter(
                    x=country_data['year'], y=country_data['co2'], fill='tozeroy', mode='lines', name=split[1]
                )
            )
        fig.update_layout(
            xaxis_title = "Year",
            yaxis_title = "CO2 Emission"
        )
        st.plotly_chart(fig, use_container_width = True)

    st.header("Area Plot by Country - (Multi-Select Country) by Population")
    data = get_countries_filter_remove_empty_column(data, 'population')
    country_options = countries_options(data)
    selected_countries = st.multiselect("Select Country: ", options = country_options, key = 'country-population-year-key')
    if selected_countries:
        fig = go.Figure()
        for selected_country in selected_countries:
            split = selected_country.split(" - ")
            country_data = data[data['iso_code'] == split[0]]
            fig.add_trace(
                go.Scatter(
                    x=country_data['year'], y=country_data['population'], fill='tozeroy', mode='lines', name=split[1]
                )
            )
        fig.update_layout(
            xaxis_title = "Year",
            yaxis_title = "Population"
        )
        st.plotly_chart(fig, use_container_width = True)
    None