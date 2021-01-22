import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import altair as alt

# Handle large data sets without embedding them in the notebook
alt.data_transformers.enable("data_server")

data = pd.read_csv(
    "../data/processed/DSCI532-CDN-CRIME-DATA-OOF.csv", sep="\t", encoding="ISO-8859-1"
)


bar_plot = alt.Chart(data).mark_bar().encode(y="GEO", x="VALUE")


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = dbc.Container(
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
                                            optionHeight=70,
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
                                            optionHeight=70,
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
                                            optionHeight=70,
                                        ),
                                    ],
                                    style={"width": "100%"},
                                ),
                            ]
                        ),
                    ],
                    width=4,
                ),
                # Column 2
                dbc.Col(
                    dbc.Row(
                        [
                            html.Div("Violation Subcategory by Province"),
                            html.Div(
                                [
                                    html.Img(
                                        src="https://i.pinimg.com/originals/27/8e/ef/278eefb576915d43e85b7a467d8f709a.jpg",
                                        width="100%",
                                    )
                                ]
                            ),
                        ]
                    ),
                    width=4,
                ),
                # Column 3
                dbc.Col(
                    dbc.Row(
                        [
                            html.Div("Violation Subcategory by CMA"),
                            html.Div(html.Iframe(srcDoc=bar_plot.to_html(),
                            height='400px')),
                        ]
                    ),
                    width=4,
                ),
            ]
        )
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)