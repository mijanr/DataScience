import streamlit as st
from sklearn import datasets
import pandas as pd
import seaborn as sns

import plotly.express as px

#set page config
page_titel = "National statistics data visualization"
page_icon = ":bar_chart:"
st.set_page_config(page_title= page_titel, page_icon= page_icon, layout="wide", initial_sidebar_state="expanded")

#load gapminder dataset
df = pd.DataFrame(px.data.gapminder())

#set header
st.header(page_titel)

#set subtitle "Countrywise data"
st.subheader("Countrywise data")

#select country from selection box and plot 
#year vs ['lifeExp', 'pop', 'gdpPercap'] upon selection
country = st.selectbox("Select country", df.country.unique())
y_axis = st.selectbox("Select y-axis", ['lifeExp', 'pop', 'gdpPercap'])

# write a function to plot the data
def plot_data(country, y_axis):
    #conditional plot
    if y_axis == 'lifeExp':
        fig = px.line(df[df.country == country], x="year", y="lifeExp", title=f"{country} - Life expectancy")
        st.plotly_chart(fig)
    elif y_axis == 'pop':
        fig = px.line(df[df.country == country], x="year", y="pop", title=f"{country} - Population")
        st.plotly_chart(fig)
    elif y_axis == 'gdpPercap':
        fig = px.line(df[df.country == country], x="year", y="gdpPercap", title=f"{country} - GDP per capita")
        st.plotly_chart(fig)

plot_data(country, y_axis)
st.write("")

#set subtitle "Continentwise data"
st.subheader("Continentwise data")

#select continent from selection box and plot
#year vs ['lifeExp', 'pop', 'gdpPercap'] upon selection
continent = st.selectbox("Select continent", df.continent.unique())
#y_axis = st.selectbox("Select y-axis", ['lifeExp', 'pop', 'gdpPercap'])

# write a function to plot the data
def plot_data(continent, y_axis):
    #conditional plot
    #first group by continent and then plot
    df_continent = df.groupby(['continent', 'year']).mean().reset_index()
    if y_axis == 'lifeExp':
        fig = px.line(df_continent[df_continent.continent == continent], x="year", y="lifeExp", title=f"{continent} - Life expectancy")
        st.plotly_chart(fig)
    elif y_axis == 'pop':
        fig = px.line(df_continent[df_continent.continent == continent], x="year", y="pop", title=f"{continent} - Population")
        st.plotly_chart(fig)
    elif y_axis == 'gdpPercap':
        fig = px.line(df_continent[df_continent.continent == continent], x="year", y="gdpPercap", title=f"{continent} - GDP per capita")
        st.plotly_chart(fig)

plot_data(continent, y_axis)
st.write("")

#set subtitle "World data"
st.subheader("World data")
#plot year vs ['lifeExp', 'pop', 'gdpPercap'] upon selection
#y_axis = st.selectbox("Select y-axis", ['lifeExp', 'pop', 'gdpPercap'])

# write a function to plot the data
def plot_data(y_axis):
    #conditional plot
    #first group by continent and then plot bars
    df_world = df.groupby(['year']).mean().reset_index()
    if y_axis == 'lifeExp':
        fig = px.bar(df_world, x="year", y="lifeExp", title="World - Life expectancy")
        st.plotly_chart(fig)
    elif y_axis == 'pop':
        fig = px.bar(df_world, x="year", y="pop", title="World - Population")
        st.plotly_chart(fig)
    elif y_axis == 'gdpPercap':
        fig = px.bar(df_world, x="year", y="gdpPercap", title="World - GDP per capita")
        st.plotly_chart(fig)

plot_data(y_axis)
st.write("")