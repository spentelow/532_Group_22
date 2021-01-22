# author: Sasha Babicki
# date: 2021-01-22

"""
Generate crime statistics dashboard with 2 tabs
Usage: python src/app.py
Based on: https://dash.plotly.com/dash-core-components/tabs
"""

import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output

import tab1

app = dash.Dash(__name__,  external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dcc.Tabs(id='crime-dashboard-tabs', value='tab-1', children=[
        dcc.Tab(label='Geographic Crime Comparisons', value='tab-1'),
        dcc.Tab(label='Crime Trends', value='tab-2'),
    ]),
    html.Div(id='crime-dashboard-content')
])

@app.callback(Output('crime-dashboard-content', 'children'),
              Input('crime-dashboard-tabs', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            tab1.generate_layout()
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab content 2')
        ])


if __name__ == '__main__':
    app.run_server(debug=True)