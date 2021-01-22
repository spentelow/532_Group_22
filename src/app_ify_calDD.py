import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import numpy as np
import pandas as pd
import altair as alt
import datetime
import dash_bootstrap_components as dbc

#Handle large data sets without embedding them in the notebook
alt.data_transformers.enable("data_server")

### Data Wrangling
df = pd.read_csv("./data/DSCI532-CDN-CRIME-DATA-CSV.csv", sep = '\t', encoding = "ISO-8859-1")
df = df.query("Metric == 'Rate per 100,000 population'")
df = df.dropna()
df['Year'] = pd.to_datetime(df['Year'], format='%Y')
df1 = df[df["Geo_Level"] == "PROVINCE"]
df_vio = df1[df1["Violation Description"] == "Total violent Criminal Code violations [100]"]
df_prop = df1[df1["Violation Description"] == "Total property crime violations [200]"]
df_other = df1[df1["Violation Description"] == "Total other Criminal Code violations [300]"]
df_drug = df1[df1["Violation Description"] == "Total drug violations [401]"]


# Setup app and layout/frontend
app = dash.Dash(external_stylesheets = [dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.Iframe(
        id = 'time-prop',
        style={'border-width': '0', 'width': '100%', 'height': '250px'}),])


app.layout = dbc.Container([
    html.H3('Crime Time Trends'),
    
    ### 1st Row 
    dbc.Row([

        ### 1st column
        dbc.Col([
            dcc.Dropdown(
              id = 'geo-widget',
              value = 'British Columbia [59]',
              multi = True, 
              options = [{'label': city, 'value': city} for city in df_prop["Geography"].unique()])],
              #labelStyle = {'display': 'block'})],
              md = 1.2),

         dbc.Col(
            html.Iframe(
                id = 'time-prop',
                style = {'border-width': '0', 'width': '100%', 'height': '800px'}))])])


@app.callback(
    Output('time-prop', 'srcDoc'),
    Input('geo-widget', 'value'))
def plot_alt1(geo_values):
    geo_list = list(geo_values)

    df_vio2 = df_vio[df_vio["Geography"].isin(geo_list)]
    chart1 = alt.Chart(df_vio2, title = "Violent Crimes").mark_line().encode(
    x = alt.X('Year'),
    y = alt.Y('Value', title = "Violations per 100k"),
    color = "Geography").properties(height = 150, width = 300)

    df_prop2 = df_prop[df_prop["Geography"].isin(geo_list)]
    chart2 = alt.Chart(df_prop2, title = "Property Crimes").mark_line().encode(
    x = alt.X('Year'),
    y = alt.Y('Value', title = "Violations per 100k"),
    color = 'Geography').properties(height = 150, width = 300)

    df_drug2 = df_drug[df_drug["Geography"].isin(geo_list)]
    chart3 = alt.Chart(df_drug2, title = "Drug Crimes").mark_line().encode(
    x = alt.X('Year'),
    y = alt.Y('Value', title = "Violations per 100k"),
    color = 'Geography').properties(height = 150, width = 300)

    df_other2 = df_other[df_other["Geography"].isin(geo_list)]
    chart4 = alt.Chart(df_drug2, title = "Other Criminal Code Violations").mark_line().encode(
    x = alt.X('Year'),
    y = alt.Y('Value', title = "Violations per 100k"),
    color = 'Geography').properties(height = 150, width = 300)

    chart = (chart1 | chart3) & (chart2 | chart4)

    return chart.to_html()


if __name__ == "__main__":
    app.run_server(debug = True)