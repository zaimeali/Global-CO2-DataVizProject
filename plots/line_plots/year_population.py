# Import Libraries
import pandas as pd
from dash import html, dcc

# Function for a Country
def country_year_population_line_plot(countries_dict, default_country):
    return html.Div([
        html.H1("Country - Year vs Population"),
        dcc.Dropdown(
            id = 'country-population-dropdown',
            options = countries_dict,
            value = default_country
        ),
        dcc.Graph(id = "country-population-graph", config = { 'scrollZoom': True })
    ])

# Function for a Callback Country
def population_graph_of_a_country_each_year(iso_code: str, df: pd.DataFrame):
    filtered_country_df = df[df['iso_code'] == iso_code]
    filtered_country = filtered_country_df['country'].iloc[0]

    first_recorded_year = filtered_country_df['year'].min() - 50
    last_recorded_year = filtered_country_df['year'].max()
    
    line_plot_figure = {
        'data': [
            {
                'x': filtered_country_df['year'],
                'y': filtered_country_df['population'],
                'type': 'line',
                'name': filtered_country
            }
        ],
        'layout': {
            'title': f'Population of {filtered_country} from Year {first_recorded_year} to {last_recorded_year}',
            'xaxis': {
                'title': 'Year'
            },
            'yaxis': {
                'title': 'Population'
            }
        }
    }

    return line_plot_figure


# Function for a Region
def region_year_population_line_plot(regions_dict, default_region):
    return html.Div([
        html.H1("Region - Year vs Population"),
        dcc.Dropdown(
            id = 'region-population-dropdown',
            options = regions_dict,
            value = default_region
        ),
        dcc.Graph(id = "region-population-graph", config = { 'scrollZoom': True })
    ])

# Function for a Callback Region
def population_graph_of_a_region_each_year(region: str, df: pd.DataFrame):
    filtered_region_df = df[df['country'] == region]
    filtered_region = filtered_region_df['country'].iloc[0]

    first_recorded_year = filtered_region_df['year'].min() - 50
    last_recorded_year = filtered_region_df['year'].max()
    
    line_plot_figure = {
        'data': [
            {
                'x': filtered_region_df['year'],
                'y': filtered_region_df['population'],
                'type': 'line',
                # 'name': filtered_region
            }
        ],
        'layout': {
            'title': f'Population of {filtered_region} from Year {first_recorded_year} to {last_recorded_year}',
            'xaxis': {
                'title': 'Year'
            },
            'yaxis': {
                'title': 'Population'
            }
        }
    }

    return line_plot_figure