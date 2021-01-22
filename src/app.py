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

import altair as alt
import pandas as pd

import tab1

app = dash.Dash(__name__,  external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Tabs(id='crime-dashboard-tabs', value='tab-1', children=[
        dcc.Tab(label='Geographic Crime Comparisons', value='tab-1'),
        dcc.Tab(label='Crime Trends', value='tab-2'),
    ]),
    html.Div(id='crime-dashboard-content')
])

@app.callback(
    Output('crime-dashboard-content', 'children'),
    Input('crime-dashboard-tabs', 'value'))
def render_content(tab):
    data = import_data()
    if tab == 'tab-1':
        return html.Div([
            tab1.generate_layout()
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab content 2')
        ])

# Pull initial data for plots
def import_data():
    """Import data from file

    Returns
    -------
    pd.Dataframe
        dataframe containing all data from the processed import file
    """
    # Handle large data sets without embedding them in the notebook
    alt.data_transformers.enable("data_server")
    
    data = pd.read_csv(
        "../data/processed/DSCI532-CDN-CRIME-DATA-OOF.csv", sep="\t", encoding="ISO-8859-1"
    )
    return data
    
DATA = import_data()

# CMA plot, tab1
@app.callback(
   Output('cma_barplot', 'srcDoc'),
   Input('metric_select', 'value'), 
   Input('violation_select', 'value'))
def generate_cma_barplot(metric, violation):
    """Create CMA barplot

    Returns
    -------
    html
        altair plot in html format
    """
    df = DATA[(DATA["Statistics"] == metric) & (DATA["Violations"] == violation)]
    
    plot = alt.Chart(df, width=250).mark_bar().encode(
        x=alt.X('VALUE', axis=alt.Axis(title=metric)),
        y=alt.Y('GEO', axis=alt.Axis(title='Census Metropolitan Area (CMA)')), 
        tooltip='VALUE'
    ).properties(
        title=violation
    ).to_html()
    return plot
 
def get_dropdown_values(col):
    """Create CMA barplot
    
    Parameters
    -------
    String
        The column to get dropdown options / value for
    
    Returns
    -------
    [[String], String]
        List with two elements, options list and default value based on data
    """
    df = DATA[col].unique()
    return [[{"label": x, "value": x} for x in df], df[0]]
      
@app.callback(
    Output('metric_select', 'options'),
    Output('metric_select', 'value'),
    Output('violation_select', 'options'),
    Output('violation_select', 'value'),
    Input('crime-dashboard-tabs', 'value'))
def set_dropdown_values(__):
    """Set dropdown options for metrics, returns options list and default value for each output"""
    dropdowns = ["Statistics", "Violations"]
    output = []
    for i in dropdowns:
        output += get_dropdown_values(i)
    return output

if __name__ == '__main__':
    
    # Allow for larger altair plots
    alt.data_transformers.enable("data_server")
    
    app.run_server(debug=True)