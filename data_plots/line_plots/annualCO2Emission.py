import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from matplotlib import pyplot as plt
import seaborn as sns


def line_chart(data: pd.DataFrame, title: str, options: dict, label: str, chart_options: dict) -> None:
    selection: str = st.selectbox(label = label, options = options, index = None)
    if not selection == None:
        selected_data = data[data['iso_code'] == selection.split(" - ")[0]]

        if selected_data['iso_code'].empty:
            selected_data = data[data['country'] == selection]

        if selected_data[chart_options['y']].isna().all():
            st.warning(f"Empty Record for {chart_options['y'].upper()} therefore, cannot plot")
        else:
            fig = px.line(
                selected_data, 
                x = chart_options['x'], 
                y = chart_options['y']
            ).update_layout(
                title_text = title + options[selection],
                xaxis_title = chart_options['x_label'],
                yaxis_title = chart_options['y_label']
            )
            st.plotly_chart(fig, use_container_width = True)

        st.write("First 5 Records:")
        st.write(selected_data.head())
        st.write("Last 5 Records:")
        st.write(selected_data.tail())
    return None

def line_chart_last_given_number_of_years(data: pd.DataFrame, title: str, options: dict, chart_options: dict) -> None:
    st.header(title)
    
    selection_country = st.selectbox(label = "Select Country: ", options = options, index = None)

    if not selection_country == None:
        selected_country = data[data['iso_code'] == selection_country.split(" - ")[0]]
        if not selected_country.empty:
            selection_year = st.select_slider("Select Last Number of Years:", options=list(range(5, 51, 5)), value=5, label_visibility="visible")

            filtered_country = selected_country.tail(selection_year)
            col1, col2 = st.columns(2)

            fig1 = px.line(
                filtered_country, x = 'year', y = 'population', title = 'Year by Population Chart'
            ).update_layout(
                xaxis_title = f'Year (gap of {selection_year} years)',
                yaxis_title = 'Population (Million to Billion)'
            )
            col1.plotly_chart(fig1)

            fig2 = px.line(
                filtered_country, x = 'year', y = 'gdp', title = 'Year by GDP Chart'
            ).update_layout(
                xaxis_title = f'Year (gap of {selection_year} years)',
                yaxis_title = 'GDP ($)'
            )
            col2.plotly_chart(fig2)

            col3, col4 = st.columns(2)
            
            fig3 = px.line(
                filtered_country, x = 'year', y = 'co2', title = 'Year by CO2 Emission Chart'
            ).update_layout(
                xaxis_title = f'Year (gap of {selection_year} years)',
                yaxis_title = 'CO2 Emission (Trillion)'
            )
            col3.plotly_chart(fig3)

            cols = ['population', 'gdp', 'co2']
            label_cols = ['Population', 'GDP', 'CO2']
            fig4 = px.imshow(
                filtered_country[cols].corr(),
                x = label_cols,
                y = label_cols
            )
            col4.plotly_chart(fig4)

            # for certain columns
            cols = ['population', 'gdp', 'co2', 'temperature_change_from_co2', 'temperature_change_from_ch4', 'primary_energy_consumption', 'oil_co2', 'energy_per_capita', 'energy_per_gdp', 'co2_per_capita', 'co2_per_gdp']
            st.write(filtered_country[cols])

            # 'temperature_change_from_c02', 'temperature_change_from_ch4', 'primary_energy_consumption', 'oil_co2', 'energy_per_capita', 'energy_per_gdp', 'co2_per_capita', 'co2_per_gdp'

            data_corr = filtered_country[cols].corr()
            cols = ['Population', 'GDP', 'CO2', 'Temperature Change from CO2', 'Temperature Change from CH4', 'Primary Energy Consumption', 'Oil CO2', 'Energy per Capita', 'Energy per GDP', 'CO2 per Capita', 'CO2 per GDP']
            fig = go.Figure(data = go.Heatmap(
                z = data_corr.values,
                x = cols,
                y = cols,
                colorscale = 'RdBu'
            ))
            fig.update_layout(
                width = 1300,
                height = 1100,
                title = "Heatmap including other features"
            )
            st.plotly_chart(fig, use_container_width = True)
    return None