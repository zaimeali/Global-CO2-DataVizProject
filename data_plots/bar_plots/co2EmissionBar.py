import pandas as pd
import streamlit as st
import plotly.express as px

def bar_chart_top_10_countries_co2_emission(dataFrame: pd.DataFrame) -> None:
    countries_df = dataFrame

    total_countries_num: int = 10
    col: str = 'gdp'
    min_year: int = countries_df['year'].min()
    max_year: int = countries_df['year'].max()
    st.title("Top 10 Countries by GDP")
    year_selected = st.slider("Select Year: ", min_year, max_year, value = min_year)
    year_selected_country_df = countries_df[countries_df['year'] == year_selected]
    top_10_gdp_year_selected_country_df = year_selected_country_df.sort_values(by = col, ascending = False).head(total_countries_num)
    
    col1, col2 = st.columns(2)
    col1.text("Top 10 GDP Countries by CO2 Emission from Coal in the Selected Year:")
    if len(list(top_10_gdp_year_selected_country_df['coal_co2'].dropna())) > 0 and sum(list(top_10_gdp_year_selected_country_df['coal_co2'].dropna())) > 0:
        fig1 = px.bar(
            top_10_gdp_year_selected_country_df,
            y = 'coal_co2',
            text = 'country',
            color = 'country',
            x = list(range(1, 1 + len(list(top_10_gdp_year_selected_country_df['coal_co2'])))),
            custom_data = 'gdp'
        )
        fig1.update_layout(
            xaxis=dict(
                tickmode="linear",
                title = "Ranking by GDP (Highest to Lowest)"
            ),
            yaxis=dict(title="CO2 Emission from Coal (kt)"),
            hovermode="x",
        )
        fig1.update_traces(hovertemplate="$%{customdata:,.0f}")
        col1.plotly_chart(fig1)
    else:
        col1.warning("No Data Found for 'Top 10 GDP Countries by CO2 Emission from Coal in the Selected Year'")
    
    col2.text("Top 10 GDP Countries by CO2 Emission from Oil in the Selected Year:")
    if len(list(top_10_gdp_year_selected_country_df['oil_co2'].dropna())) > 0 and sum(list(top_10_gdp_year_selected_country_df['oil_co2'].dropna())) > 0:
        fig2 = px.bar(
            top_10_gdp_year_selected_country_df,
            y = 'oil_co2',
            text = 'country',
            color = 'country',
            x = list(range(1, 1 + len(list(top_10_gdp_year_selected_country_df['oil_co2'])))),
            custom_data = 'gdp'
        )
        fig2.update_layout(
            xaxis=dict(
                tickmode="linear",
                title = "Ranking by GDP (Highest to Lowest)"
            ),
            yaxis=dict(title="CO2 Emission from Oil (kt)"),
            hovermode="x",
        )
        fig2.update_traces(hovertemplate="$%{customdata:,.0f}")
        col2.plotly_chart(fig2)
    else:
        col2.warning("No Data Found for 'Top 10 GDP Countries by CO2 Emission from Oil in the Selected Year'")

    st.text("Top 10 GDP Countries by CO2 Emission from Other Industry in the Selected Year:")
    if len(list(top_10_gdp_year_selected_country_df['other_industry_co2'].dropna())) > 0 and sum(list(top_10_gdp_year_selected_country_df['other_industry_co2'].dropna())) > 0:
        fig = px.bar(
            top_10_gdp_year_selected_country_df,
            y = 'other_industry_co2',
            text = 'country',
            color = 'country',
            x = list(range(1, 1 + len(list(top_10_gdp_year_selected_country_df['other_industry_co2'])))),
            custom_data = 'gdp'
        )
        fig.update_layout(
            xaxis=dict(
                tickmode="linear",
                title = "Ranking by GDP (Highest to Lowest)"
            ),
            yaxis=dict(title="CO2 Emission from Other Industry (kt)"),
            hovermode="x",
        )
        fig.update_traces(hovertemplate="$%{customdata:,.0f}")
        st.plotly_chart(fig, use_container_width = True)
    else:
        st.warning("No Data Found for 'Top 10 GDP Countries by CO2 Emission from Other Industry in the Selected Year'")