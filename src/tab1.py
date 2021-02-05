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
    start_year = 1998
    end_year = 2019
    year_range = list(range(start_year, end_year+1,3))
    slider_marks = dict(zip(
        year_range,
        [str(x) for x in year_range]
         ))
    
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
                                            "Select Year of Interest",
                                            dcc.RangeSlider(
                                                id="year_select",
                                                min = start_year, 
                                                max = end_year,
                                                step = 1,
                                                value =[1998,2019], 
                                                dots = True,
                                                tooltip = {"placement": "top"},
                                                marks = slider_marks
                                                )
                                        ], 
                                        style = {"width": "100%"},
                                    ),
                                ]
                            ),
                            html.Br(),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        [
                                            html.H5("About this Dashboard"),
                                            html.Br(),
                                            html.P("""
                                            One advanced diverted domestic sex repeated bringing you old. 
                                            Possible procured her trifling laughter thoughts property she met way. 
                                            Companions shy had solicitude favourable own. Which could saw guest man now heard but. 
                                            Lasted my coming uneasy marked so should. Gravity letters it amongst herself dearest an windows by. 
                                            Wooded ladies she basket season age her uneasy saw. Discourse unwilling 
                                            am no described dejection incommode no listening of. Before nature his parish boy. 
                                            """,
                                            style = {'color': 'grey'})    
                                        ]
                                    )
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