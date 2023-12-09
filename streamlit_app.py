# Import Libraries
import pandas as pd
import streamlit as st

from utils.enrich_data import get_countries, countries_options, get_regions, regions_options, get_clean_countries, get_top_n_numbers_of_countries
from data_plots.line_plots.annualCO2Emission import line_chart, line_chart_last_given_number_of_years
from data_plots.area_plots.annualCO2Emission import area_plot_by_region, area_plot_multi_select_country
from data_plots.map_plots.globalCO2Emission import plot_map_global_co2_emission
from data_plots.bar_plots.co2EmissionBar import bar_chart_top_10_countries_co2_emission

# Import Data
data = pd.read_csv('./co2-global-data.csv', header = 0)

if __name__ == '__main__':
    st.set_page_config(layout="wide")

    # Plot Line Graph for Country
    st.header("Annual CO2 Emission Line Graph of Country")
    chart_options = {
        'x': "year",
        'x_label': "Year",
        'y': 'co2',
        'y_label': "CO2 Emission (in Billions tons)"
    }
    line_chart(data, "Annual CO2 Emission of ", countries_options(get_countries(data)), "Select Country: ", chart_options)
    st.divider()

    # Plot Line Graph for Region
    st.header("Annual CO2 Emission Line Graph of Region")
    line_chart(data, "Annual CO2 Emission of ", regions_options(get_regions(data)), "Select Region: ", chart_options)
    st.divider()

    # Plot Area Graph for Region
    area_plot_by_region(get_regions(data))
    st.divider()

    area_plot_multi_select_country(data)
    st.divider()

    line_chart_last_given_number_of_years(data, "Data Record of a Country with Number of Years", countries_options(get_clean_countries(get_countries(data), ['year', 'gdp', 'co2', 'population'])), None)
    st.divider()

    # map
    plot_map_global_co2_emission(data, "Global CO2 Emission")
    st.divider()

    # bar chart
    bar_chart_top_10_countries_co2_emission(get_top_n_numbers_of_countries(data))
    # if to start from new, I would integrate import export data