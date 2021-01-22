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

df = pd.read_csv("./data/DSCI532-CDN-CRIME-DATA-CSV.csv", sep = '\t', encoding = "ISO-8859-1")
df['Year'] = pd.to_datetime(df['Year'], format='%Y')

#df_violence = df[df["Violation Description"] == "Total violent Criminal Code violations [100]"]
df_property = df[df["Violation Description"] == "Total property crime violations [200]"]
#df_other = df[df["Violation Description"] == "Total other Criminal Code violations [300]"]
#df_drugs = df[df["Violation Description"] == "Total drug violations [401]"]

app = dash.Dash(__name__, external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'])


#app.layout = dbc.Container([
#    html.Iframe(
#        id = 'scatter',
#        style = {'border-width' : '0', 'width' : "100%",
#        'height' : '400px'}),
#        dcc.Dropdown(
#            id = 'xcol-widget',
#            value = "Year", 
#            options = [{'label': i, 'value': i} for i in df.columns])
#])


### Set up callbacks/backend
#@app.callback(
#    Output('scatter', 'srcDoc'),
#    Input('xcol-widget', 'value'))
#def time_plot(data, title_name, xmax = 'Year'):
#    chart = alt.Chart(data, title = title_name).mark_line().encode(
#    y = alt.Y('Value', title = "Violations per 100k"),
#    x = xmax,
#    color = "Geography",
#    tooltip = "Geography").interactive()
#    return chart.to_html()


def time_plot(data, title_name):
    chart = alt.Chart(data, title = title_name).mark_line().encode(
    y = alt.Y('Value', title = "Violations per 100k"),
    x = "Year",
    color = "Geography",
    tooltip = "Geography").properties(height = 200, width = 300)
    return chart.to_html()


app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

app.layout = html.Div([
        html.Iframe(
            id='scatter',
            srcDoc = time_plot(df_property, "Property Crimes"),
            style = {'border-width': '0', 'width': '100%', 'height': '400px'}),
        dcc.Slider(id='xslider', min=0, max=240)])

@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xslider', 'value'))
def update_output():
    return time_plot(df_property, "Property Crimes")



#x = datetime.datetime(2020, 5, 17)

#plot_property = time_plot(df_property, "Property Crimes")
#plot_other = time_plot(df_other, "Other Criminal Code Violations")
#plot_drugs = time_plot(df_drugs, "Drug Crimes")




if __name__ == "__main__":
    app.run_server(debug = True)