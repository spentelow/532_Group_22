import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import numpy as np
import pandas as pd
import altair as alt
import datetime
import dash_bootstrap_components as dbc

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

def generate_layout():
    """Generate tab 1 layout

    Returns
    -------
    dbc.Container
        Container with the html content of the page
    """
    
    return dbc.Container([
        html.H3('Crime Time Trends'),

        ### 1st Row 
        dbc.Row([
            ### 1st column
            dbc.Col([
                dcc.Dropdown(
                  id = 'cma_multi_select',
                  multi = True, 
                  options = [{'label': city, 'value': city} for city in df_prop["Geography"].unique()],
                  value = 'British Columbia [59]'
                  #labelStyle = {'display': 'block'})],
                  )
              ]),
              dbc.Col([
                html.Iframe(
                    id = 'crime_trends_plot',
                    style = {'border-width': '0', 'width': '100%', 'height': '800px'}
                )
            ])
        ])
    ])