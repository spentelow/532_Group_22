# author: Sasha Babicki, Ifeanyi Anene, and Cal Schafer 
# date: 2021-01-22

"""
Generate crime statistics dashboard with 2 tabs
Usage: python src/app.py
Source for code to create tabs: https://dash.plotly.com/dash-core-components/tabs
"""

import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import dash_leaflet as dl
from dash_extensions.javascript import Namespace, arrow_function

import altair as alt
import pandas as pd
import json

import tab1
import tab2

app = dash.Dash(__name__,  external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
app.title = 'Canadian Crime Dashboard'
server = app.server

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
            tab2.generate_layout()
        ])

# Pull initial data for plots
def import_data():
    """Import data from file

    Returns
    -------
    pd.Dataframe
        dataframe containing all data from the processed import file
    """
    # Disable max rows for data sent to altair plots
    alt.data_transformers.disable_max_rows()
    
    path = "data/processed/DSCI532-CDN-CRIME-DATA.tsv"
    data = pd.read_csv(path, sep="\t", encoding="ISO-8859-1")
    
    ### Data Wrangling 
    data = data.dropna()
    data.replace(" \[.*\]", "", regex=True, inplace=True)
    return data
    
DATA = import_data()

def import_map():
    """Import map data from file

    Returns
    -------
    json
        geojson for provinces
    """
    with open("data/processed/canada_provinces.geojson") as f:
        geojson = json.load(f)
    return geojson

PROVINCES = import_map()

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
    year = 2002 # TODO: connect year to slider
    df = DATA[
        (DATA["Metric"] == metric) & 
        (DATA["Violation Description"] == violation) &
        (DATA['Year'] == year) &
        (DATA['Geo_Level'] == "CMA")
    ]
    
    plot = alt.Chart(df, width=250).mark_bar().encode(
        x=alt.X('Value', axis=alt.Axis(title=metric)),
        y=alt.Y('Geography', axis=alt.Axis(title='Census Metropolitan Area (CMA)'), sort='-x'), 
        tooltip='Value'
    ).properties(
        title=violation
    ).to_html()
    return plot

# TODO: Move these references somewhere more visible
# Canadian provinces map from: https://exploratory.io/map 
# Tutorial used: https://dash-leaflet.herokuapp.com/#geojson 
@app.callback(
   Output('choropleth', 'children'),
   Input('metric_select', 'value'), 
   Input('violation_select', 'value'))
def generate_choropleth(metric, violation):    
    year = 2002 # TODO: connect year to slider
    geojson = PROVINCES
    df = DATA [
        (DATA["Metric"] == metric) & 
        (DATA["Violation Description"] == violation) &
        (DATA["Year"] == year) &
        (DATA['Geo_Level'] == "PROVINCE")
    ]
    
    data_dict = dict(zip(df['Geography'], df['Value']))
    
    for location in geojson['features']:
        try:
            lookup_val = data_dict[location['properties']['PRENAME']]
        except:
            lookup_val = None
        location['properties']['Value'] = lookup_val
        
    # TODO: Set colour scale and better break points
    vals = pd.Series(data_dict.values())
    classes = list(range(int(vals.min()), int(vals.max()), int(vals.max()/len(vals)))) 
    colorscale = ['#FFEDA0', '#FED976', '#FEB24C', '#FD8D3C', '#FC4E2A', '#E31A1C', '#BD0026', '#800026']
    style = dict(weight=1, color='black', fillOpacity=0.7)
    hover_style = dict(weight=5, color='orange', dashArray='')
    ns = Namespace("dlx", "choropleth")    
    
    # TODO: Add Legend
    return [ 
        dl.TileLayer(),
        dl.GeoJSON(data=geojson, id="provinces", 
        options=dict(style=ns("style")),
        hideout=dict(colorscale=colorscale, classes=classes, style=style, colorProp="Value"),
        hoverStyle=arrow_function(hover_style))
    ]

# Effect of hovering over province. Alternative: click_feature
@app.callback(
    Output("province_info", "children"), 
    Input("provinces", "hover_feature"))
def capital_click(feature):
    if feature is not None:
        return f"{feature['properties']['PRENAME']}: {feature['properties']['Value']}"
    else:
        return "Hover over a Province to view details"

@app.callback(
    Output('crime_trends_plot', 'srcDoc'),
    Input('geo_multi_select', 'value'),
    Input('geo_radio_button', 'value'))
def plot_alt1(geo_list, geo_level):
    
    metric = "Violations per 100k"
    metric_name = "Violations per 100k"
    
    df = DATA[
        (DATA['Metric'] == 'Rate per 100,000 population') &
        (DATA["Geo_Level"] == geo_level) 
    ]
    df = df[df["Geography"].isin(geo_list)]
    
    category_dict = {
        'Violent Crimes' : 'Total violent Criminal Code violations',
        'Property Crimes' : 'Total property crime violations',
        'Drug Crimes' : 'Total drug violations',
        'Other Criminal Code Violations' : 'Total other Criminal Code violations'
    }
    
    plot_list = []
    
    for title, description in category_dict.items():
        plot_list.append(
            alt.Chart(df[df['Violation Description'] == description], title = title).mark_line().encode(
                x = alt.X('Year'),
                y = alt.Y('Value', title = metric_name),
                tooltip = 'Value',
                color = 'Geography').properties(height = 150, width = 300)
        )

    chart = (plot_list[0] | plot_list[2]) & (plot_list[1] | plot_list[3])

    return chart.to_html()

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
    dropdowns = ["Metric", "Violation Description"]
    output = []
    for i in dropdowns:
        output += get_dropdown_values(i)
    return output
    
@app.callback(
    Output('geo_multi_select', 'options'),
    Input('crime-dashboard-tabs', 'value'),    
    Input('geo_radio_button', 'value'))
def set_multi_dropdown_values(__, geo_level):
    """Set dropdown options for metrics, returns options list  for each output"""
    
    df = DATA[DATA["Geo_Level"] == geo_level]
    df = df["Geography"].unique()
    return [{'label': city, 'value': city} for city in df]

if __name__ == '__main__':
    
    # Disable max rows for data sent to altair plots
    alt.data_transformers.disable_max_rows()
    
    app.run_server(debug=True)