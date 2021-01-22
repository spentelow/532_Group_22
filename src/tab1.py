# author: Steffen Pentelow and Sasha Babicki
# date: 2021-01-22
"""
Module to generate tab 1: Geographic Crime Comparisons
"""

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import altair as alt

def import_data():
    """Import data from file

    Returns
    -------
    pd.Dataframe
        dataframe containing all data from the processed import file
    """
    data = pd.read_csv(
        "../data/processed/DSCI532-CDN-CRIME-DATA-OOF.csv", sep="\t", encoding="ISO-8859-1"
    )
    return data

def generate_cma_barplot(data):
    """Create CMA barplot

    Returns
    -------
    html
        altair plot in html format
    """
    return alt.Chart(data, width=250).mark_bar().encode(y="GEO", x="VALUE", tooltip="VALUE").to_html()
    
def generate_layout():
    """Generate tab 1 layout

    Returns
    -------
    dbc.Container
        Container with the html content of the page
    """
    
    dropdown_height = 70
    
    # Handle large data sets without embedding them in the notebook
    alt.data_transformers.enable("data_server")

    data = import_data()

    return dbc.Container(
        [
            dbc.Row(
                [
                    # Column 1
                    dbc.Col(
                        [
                            dbc.Row(
                                [
                                    html.Div(
                                        [
                                            "Select Metric",
                                            dcc.Dropdown(
                                                id="metric_select",
                                                options=[
                                                    {"label": x, "value": x}
                                                    for x in data["Statistics"].unique()
                                                ],
                                                optionHeight=dropdown_height,
                                            ),
                                        ],
                                        style={"width": "100%"},
                                    ),
                                ]
                            ),
                            dbc.Row(
                                [
                                    html.Div(
                                        [
                                            "Select Violation",
                                            dcc.Dropdown(
                                                id="vio_select",
                                                options=[
                                                    {"label": x, "value": x}
                                                    for x in data["Violations"].unique()
                                                ],
                                                optionHeight=dropdown_height,
                                            ),
                                        ],
                                        style={"width": "100%"},
                                    ),
                                ]
                            ),
                            dbc.Row(
                                [
                                    html.Div(
                                        [
                                            "Select Violation Subcategory",
                                            dcc.Dropdown(
                                                id="subvio_select",
                                                options=[
                                                    {
                                                        "label": "NotYetImplemented",
                                                        "value": "Dummy",
                                                    }
                                                ],
                                                # options=[
                                                #     {'label': x, 'value': x} for x in data['Violations'].unique()
                                                # ],
                                                optionHeight=dropdown_height,
                                            ),
                                        ],
                                        style={"width": "100%"},
                                    ),
                                ]
                            ),
                        ],
                        style={'padding-left': '2%'}
                    ),
                    
                    # Column 2
                    dbc.Col(
                        dbc.Row(
                            [
                                html.Div("Violation Subcategory by Province"),
                                html.Div(
                                    [
                                        html.Img( src="https://i.pinimg.com/originals/27/8e/ef/278eefb576915d43e85b7a467d8f709a.jpg",
                                            width="100%",
                                        )
                                    ]
                                ),
                            ]
                        ),
                        style={'padding-left': '2%'}
                    ),
                    
                    # Column 3
                    dbc.Col(
                        dbc.Row(
                            [
                                html.Div("Violation Subcategory by CMA"),
                                html.Iframe(
                                    id='cma-barplot',
                                    srcDoc = generate_cma_barplot(data),
                                    style = {'border-width': '0', 'width': '100%', 'height': '600px'}
                                )
                            ]
                        ),
                        width="auto",
                        style={'padding-left': '2%', 'padding-right': '2%'}
                    ),
                ]
            )
        ], 
        fluid=True
    )