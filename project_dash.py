# Import Libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import dash
from dash import html, dcc
from dash.dependencies import Input, Output

# Utils
from plots.data.data import (
    countries_options_dict, 
    region_options_dict
)
from plots.line_plots.year_population import (
    country_year_population_line_plot, 
    population_graph_of_a_country_each_year, 
    region_year_population_line_plot,
    population_graph_of_a_region_each_year
)


# Initialize
app = dash.Dash(__name__)

# Import Data
df = pd.read_csv('./co2-global-data.csv')

default_country = 'USA'
default_region = 'World'

app.layout = html.Div([
    country_year_population_line_plot(countries_options_dict(df), default_country),
    html.Hr(),
    region_year_population_line_plot(region_options_dict(df), default_region)

    # html.H1("Region - Year vs GDP ($)"),
    # dcc.Dropdown(
    #     id = 'country-gdp-dropdown',
    #     options = countries_dict,
    #     value = default_country
    # ),
    # dcc.Graph(id = "country-gdp-graph", config = { 'scrollZoom': True }),
    # html.Hr(),

    # html.H1("Country - Year vs GDP ($)"),
    # dcc.Dropdown(
    #     id = 'country-gdp-dropdown',
    #     options = countries_dict,
    #     value = default_country
    # ),
    # dcc.Graph(id = "country-gdp-graph", config = { 'scrollZoom': True }),
    # html.Hr(),

    # html.H1("Region - Year vs GDP ($)"),
    # dcc.Dropdown(
    #     id = 'country-gdp-dropdown',
    #     options = countries_dict,
    #     value = default_country
    # ),
    # dcc.Graph(id = "country-gdp-graph", config = { 'scrollZoom': True }),
    # html.Hr(),

    # html.H1("Country - Year vs CO2 Emissions"),
    # dcc.Dropdown(
    #     id = 'country-gdp-dropdown',
    #     options = countries_dict,
    #     value = default_country
    # ),
    # dcc.Graph(id = "country-gdp-graph", config = { 'scrollZoom': True }),
    # html.Hr(),

    # html.H1("Region - Year vs CO2 Emissions"),
    # dcc.Dropdown(
    #     id = 'country-gdp-dropdown',
    #     options = countries_dict,
    #     value = default_country
    # ),
    # dcc.Graph(id = "country-gdp-graph", config = { 'scrollZoom': True }),
    # html.Hr(),

    # html.H1("Top 10 Highest GDP"),
    # html.H1("Top 10 Lowest GDP")
])

@app.callback(
    Output("country-population-graph", "figure"),
    [Input("country-population-dropdown", "value")]
)
def population_graph_of_a_country_each_year_callback(iso_code: str):
    return population_graph_of_a_country_each_year(iso_code, df)

@app.callback(
    Output("region-population-graph", "figure"),
    [Input("region-population-dropdown", "value")]
)
def population_graph_of_a_region_each_year_callback(region: str):
    return population_graph_of_a_region_each_year(region, df)

# @app.callback(
#     Output("country-population-graph", "figure"),
#     [Input("country-population-dropdown", "value")]
# )
# def population_graph_of_a_country_each_year(iso_code: str):
#     filtered_country_df = df[df['iso_code'] == iso_code]
#     filtered_country = filtered_country_df['country'].iloc[0]

#     first_recorded_year = filtered_country_df['year'].min() - 50
#     last_recorded_year = filtered_country_df['year'].max()
    
#     line_plot_figure = {
#         'data': [
#             {
#                 'x': filtered_country_df['year'],
#                 'y': filtered_country_df['population'],
#                 'type': 'line',
#                 'name': filtered_country
#             }
#         ],
#         'layout': {
#             'title': f'Population of {filtered_country} from Year {first_recorded_year} to {last_recorded_year}',
#             'xaxis': {
#                 'title': 'Year'
#             },
#             'yaxis': {
#                 'title': 'Population'
#             }
#         }
#     }

#     return line_plot_figure

# @app.callback(
#     Output("country-gdp-graph", "figure"),
#     [Input("country-gdp-dropdown", "value")]
# )
# def gdp_graph_of_a_country_each_year(iso_code: str):
#     filtered_country_df = df[df['iso_code'] == iso_code]
#     filtered_country = filtered_country_df['country'].iloc[0]

#     first_recorded_year = filtered_country_df['year'].min() - 50
#     last_recorded_year = filtered_country_df['year'].max()
    
#     line_plot_figure = {
#         'data': [
#             {
#                 'x': filtered_country_df['year'],
#                 'y': filtered_country_df['gdp'],
#                 'type': 'line',
#                 'name': filtered_country
#             }
#         ],
#         'layout': {
#             'title': f'GDP ($) of {filtered_country} from Year {first_recorded_year} to {last_recorded_year}',
#             'xaxis': {
#                 'title': 'Year'
#             },
#             'yaxis': {
#                 'title': 'GDP ($)'
#             }
#         }
#     }

#     return line_plot_figure

# Run App
if __name__ == '__main__':
    app.run_server(debug = True, port = 8091)