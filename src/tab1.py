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
import dash_leaflet as dl

def generate_layout():
    """Generate tab 1 layout

    Returns
    -------
    dbc.Container
        Container with the html content of the page
    """
    
    dropdown_height = 70
    
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
                                                optionHeight=dropdown_height,
                                            ),
                                        ],
                                        style={"width": "100%"},
                                    ),
                                ]
                            ),
                            html.Br(),
                            dbc.Row(
                                [
                                    html.Div(
                                        [
                                            "Select Violation",
                                            dcc.Dropdown(
                                                id="violation_select",
                                                optionHeight=dropdown_height,
                                            ),
                                        ],
                                        style={"width": "100%"},
                                    ),
                                ]
                            ),
                            html.Br(),
                            dbc.Row(
                                [
                                    html.Div(
                                        [
                                            "Select Violation Subcategory",
                                            dcc.Dropdown(
                                                id="subviolation_select",
                                                options=[
                                                    {
                                                        "label": "Not Implemented Yet",
                                                        "value": "Dummy",
                                                    }
                                                ],
                                                optionHeight=dropdown_height,
                                            ),
                                        ],
                                        style={"width": "100%"},
                                    ),
                                ]
                            )
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
                                        #dcc.Graph(id="choropleth"),
                                        dl.Map(id="choropleth", 
                                        center=[62, -98],
                                        zoom=3,
                                        style={'width': '550px', 'height': '600px'}),
                                        html.Div(id="province_info",className="info",
                                            style={"position": "absolute", 
                                                "top": "40px", 
                                                "right": "2%", 
                                                "z-index": "1000"})
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
                                    id='cma_barplot',
                                    style={'border-width': '0', 'width': '100%', 'height': '800px'}
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