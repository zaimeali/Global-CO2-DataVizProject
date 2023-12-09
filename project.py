# Import Libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import streamlit as st

# Import Data
df = pd.read_csv("./co2-global-data.csv", header = 0)
st.write(df.head())

region_default_value = "World"
regions = df['country'].unique()

regions_list = list(regions)

selected_region = st.selectbox('You selected Country/Region:', regions_list, index = regions_list.index(region_default_value))

st.write('You selected:', selected_region)

region = df[df['country'] == selected_region]

fig, ax = plt.subplots()
sns.lineplot(
    x = 'year',
    y = 'population',
    data = region,
    ax = ax
)
ax.set_xticks(range(region['year'][0], region['year'][-1]))
st.pyplot(fig)