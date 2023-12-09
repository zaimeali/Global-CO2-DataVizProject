import pandas as pd

# Get Countries Option for Dropdown
def countries_options(df: pd.DataFrame) -> dict:
    countries_dict = dict()

    for _, row in df.drop_duplicates(subset = ['country']).iterrows():
        country = row['country']
        iso_code = str(row['iso_code']) + " - " + str(country)

        countries_dict[iso_code] = country

    return countries_dict

# Get Regions Option for Dropdown
def regions_options(df: pd.DataFrame) -> dict:
    regions_dict = dict()

    for _, row in df.drop_duplicates(subset = ['country']).iterrows():
        country = row['country']
        iso_code = row['country']

        regions_dict[iso_code] = country

    return regions_dict

# Get Countries DataFrame
def get_countries(df: pd.DataFrame) -> pd.DataFrame:
    return df[df['iso_code'].notna()]

# Get Region DataFrame
def get_regions(df: pd.DataFrame) -> pd.DataFrame:
    return df[df['iso_code'].isnull() & df['country'].notna()]

def get_all_countries_iso_list(df: pd.DataFrame) -> list:
    return list(df[df['iso_code'].notna()].drop_duplicates(subset = ['iso_code'])['iso_code'])

def get_countries_filter_remove_empty_column(df: pd.DataFrame, filter_col: str) -> pd.DataFrame:
    iso_codes_list = get_all_countries_iso_list(df)
    df = get_countries(df)
    iso_codes_to_remove = [iso_code for iso_code in iso_codes_list if df[df['iso_code'] == iso_code][filter_col].isna().all()]
    for iso_code in iso_codes_to_remove:
        df = df.drop(df[df['iso_code'] == iso_code].index)
    return df

def get_clean_countries(df: pd.DataFrame, colsArr: list) -> pd.DataFrame:
    countries_df: pd.DataFrame = get_countries(df)
    countries_iso_list: list = get_all_countries_iso_list(df)

    filtered_countries_df: pd.DataFrame = pd.DataFrame()

    for country_iso in countries_iso_list:
        country_df: pd.DataFrame = countries_df[countries_df["iso_code"] == country_iso]
        for cols in colsArr:
            country_df = country_df[country_df[cols].notnull()]
        filtered_countries_df = pd.concat([filtered_countries_df, country_df])

    return filtered_countries_df

def get_last_selected_years_countries(df: pd.DataFrame, year: int) -> pd.DataFrame:
    countries_df: pd.DataFrame = get_countries(df)
    countries_iso_list: list = get_all_countries_iso_list(df)

    filtered_countries_df: pd.DataFrame = pd.DataFrame()

    for country_iso in countries_iso_list:
        country_df: pd.DataFrame = countries_df[countries_df["iso_code"] == country_iso]
        country_df = country_df[country_df['year'].notnull()]
        country_df = country_df[country_df['gdp'].notnull()]
        country_df = country_df[country_df['co2'].notnull()]
        if not country_df.empty:
            filtered_countries_df = pd.concat([filtered_countries_df, country_df.tail(year)])

    return filtered_countries_df

def get_top_n_numbers_of_countries(df: pd.DataFrame) -> pd.DataFrame:
    countries_df: pd.DataFrame = get_countries(df)
    countries_iso_list: list = get_all_countries_iso_list(df)

    filtered_countries_df: pd.DataFrame = pd.DataFrame()

    for country_iso in countries_iso_list:
        country_df: pd.DataFrame = countries_df[countries_df["iso_code"] == country_iso]
        country_df = country_df[country_df['year'].notnull()]
        country_df = country_df[country_df['gdp'].notnull()]
        country_df = country_df[country_df['co2'].notnull()]
        if not country_df.empty:
            filtered_countries_df = pd.concat([filtered_countries_df, country_df])
    return filtered_countries_df
