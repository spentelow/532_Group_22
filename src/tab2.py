import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import numpy as np
import pandas as pd
import altair as alt
import datetime
import dash_bootstrap_components as dbc

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
                dbc.Row(
                    [
                        dcc.RadioItems(
                            options=[
                                {'label': 'Province', 'value': 'PROVINCE'},
                                {'label': 'CMA', 'value': 'CMA'},
                            ],
                            value='PROVINCE'
                        )
                    ]
                ),
                dbc.Row(
                    [
                        dcc.Dropdown(
                            id = 'geo_multi_select',
                            multi = True, 
                            #labelStyle = {'display': 'block'})],
                        ),
                    ]
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