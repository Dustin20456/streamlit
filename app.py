import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

#set title
st.title('International Life Expectancies')

#caching data
def fetch_data():
    #data = pd.read_csv('c:/Users/Dustin/docker/streamlit/merged_data.csv')
    data = pd.read_csv('merged_data.csv')
    data['log_gni'] = np.log10(data['GNI per captia'])
    return data

df = fetch_data()


#set min and max value for slider depending on min and max value of dataframe
lower = int(df['year'].min())

upper = int(df['year'].max())

#create filter with slider widget

subset_data = df
year_to_filter = st.slider('Year', lower, upper)
subset_data = df[df['year'] == year_to_filter]

#create filter with multiselect widget
subset_data2 = subset_data
country_name_input = st.multiselect(
'Country name',
subset_data.groupby('country').count().reset_index()['country'].tolist())
# by country name
if len(country_name_input) > 0:
    subset_data2 = subset_data[subset_data['country'].isin(country_name_input)]

# create bubble chart

chart = alt.Chart(subset_data2).mark_circle().encode(
    alt.X('log_gni:Q', scale=alt.Scale(domain=[2.0,5.5])),
    alt.Y('life expectancy:Q', scale=alt.Scale(domain=[40,90])), 
    size='population', 
    color='country')

st.altair_chart(chart.properties(width=700, height=400), use_container_width=True)
