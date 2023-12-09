def countries_options_dict(df):
    countries_iso = df['iso_code'].dropna().unique()
    countries = df[df['iso_code'].isin(countries_iso)]['country'].unique()
    countries_dict = [{'label': country, 'value': iso_code} for country, iso_code in zip(countries, countries_iso)]

    return countries_dict

def region_options_dict(df):
    regions = df[df.iso_code.isna()]['country'].unique()
    regions_dict = [{'label': region, 'value': region} for region in regions]

    return regions_dict

    