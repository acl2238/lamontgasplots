# Make sure to pip install all requirements!
from IPython.display import display
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import flask

import dash # pip install dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

server = flask.Flask(__name__)

app = dash.Dash(__name__, server=server) # Starting the app

# Manually choosing input file, reading in the data as a csv
input_file = "/local/data/solasd/plot_merge_for_nyaaq" # Probably want to automate this
data = input_file + ".txt"
df = pd.read_csv(data)

#CH4 plot
fig = px.line(df, x = 'UTC_time', y = ['CH4_ppb_asrc','CH4_ppb_rutgers','CH4_ppb_mineola','CH4_ppb_ldeo'], title = '<b>Methane (CH4) in parts per billion over time</b>',
            labels = {
                'UTC_time':'Date and Time (UTC)',
            })

#CO2 plot
fig2 = px.line(df, x = 'UTC_time', y = ['CO2_ppm_asrc','CO2_ppm_rutgers','CO2_ppm_mineola','CO2_ppm_ldeo'], title = '<b>Carbon Dioxide (CO2) in parts per million over time</b>',
            labels = {
                'UTC_time':'Date and Time (UTC)',
            })

#CO plot
fig3 = px.line(df, x = 'UTC_time', y = ['CO_ppb_asrc','CO_ppb_rutgers','CO_ppb_mineola'], title = '<b>Carbon Monoxide (CO) in parts per billion over time</b>',
            labels = {
                'UTC_time':'Date and Time (UTC)',
            })
# Unfortuantely px does not natively support double axis plots
# Therefore this code is a teeny bit longer because use plotly graph objs
# In future maybe plotly locks in and fixes this :(

# Correlation plots
# All 3 subplots are part of fig 8
fig4 = make_subplots(rows=1, cols=3,
                     subplot_titles=('<b>CH4 (ppm) vs CO (ppb)</b>',
                                     '<b>CO2 (ppm) vs CO (ppb)</b>',
                                     '<b>CH4 (ppm) vs CO2 (ppm)</b>'))

# CO vs CH4
fig4.add_trace(
    go.Scatter(x=df['CO_ppb_asrc'], y=df['CH4_ppb_asrc'] / 1000,mode="markers",name="<b>CO vs CH4 ASRC</b>"),
               row=1, col=1,
)
fig4.add_trace(
    go.Scatter(x=df['CO_ppb_rutgers'], y=df['CH4_ppb_rutgers'] / 1000,mode="markers",name="<b>CO vs CH4 Rutgers</b>"),
               row=1, col=1
)
# CO vs CO2
fig4.add_trace(
    go.Scatter(x=df['CO_ppb_asrc'], y=df['CO2_ppm_asrc'],mode="markers",name="<b>CO vs CO2 ASRC</b>"),
               row=1, col=2,
)
fig4.add_trace(
    go.Scatter(x=df['CO_ppb_rutgers'], y=df['CO2_ppm_rutgers'],mode="markers",name="<b>CO vs CO2 Rutgers</b>"),
               row=1, col=2,
)
fig4.add_trace(
    go.Scatter(x=df['CO2_ppm_asrc'], y=df['CH4_ppb_asrc'] / 1000,mode="markers",name="<b>C02 vs CH4 ASRC</b>"),
               row=1, col=3,
)
fig4.add_trace(
    go.Scatter(x=df['CO2_ppm_rutgers'], y=df['CH4_ppb_rutgers'] / 1000,mode="markers",name="<b>C02 vs CH4 Rutgers</b>"),
               row=1, col=3,
)
fig4.update_layout(
    title_text = "<b>Correlation Plots for CH4, CO2, CO</b>"
)

fig4.update_layout(legend= {'itemsizing': 'constant'})

fig4.update_xaxes(title_text="CO (ppb)", row=1, col=1)
fig4.update_xaxes(title_text="CO (ppb)", row=1, col=2)
fig4.update_xaxes(title_text="CO2 (ppm)", row=1, col=3)

fig4.update_yaxes(title_text="CH4 (ppm)", row=1, col=1)
fig4.update_yaxes(title_text="CO2 (ppm)", row=1, col=2)
fig4.update_yaxes(title_text="CH4 (ppm)", row=1, col=3)


# Look into the app.layout formatting

# Font formatting (text size)
fig.update_layout(font=dict(size=20), yaxis_title = 'Methane/CH4 (ppb)',
                  legend_title_text='Data Source',
                  xaxis = dict(rangeslider=dict(visible=True)))
                  # Append above line to each fig.update_layout for horizontal scrollbars
fig2.update_layout(font=dict(size=20), yaxis_title = 'Carbon Dioxide/CO2 (ppm)',
                   legend_title_text='Data Source',
                   xaxis = dict(rangeslider=dict(visible=True)))
fig3.update_layout(font=dict(size=20), yaxis_title = 'Carbon Monoxide/CO (ppb)',
                   legend_title_text='Data Source',
                   xaxis = dict(rangeslider=dict(visible=True)))
fig4.update_layout(font=dict(size=16))


app.layout = html.Div(children=[

    html.Div([
        html.H1("NYAAQ Network Site Observations", style={'text-align': 'center', 'font-size':'72px'}),
        html.H1("Graphs are interactive!", style={'text-align':'center'}),
        html.H2("""Hover over lines to see exact values,
                highlight to zoom, and hide/show values in the
                plots by selecting them in the legend!""",
                style={'text-align':'center'}),
        html.H2("""Additionally, drag the range sliders below each graph
                to specify timeframe for shown data!""", style={'text-align':'center'}),
        dcc.Graph(figure=fig),
    ]),
    html.Div([
        dcc.Graph(figure=fig2),
    ]),
    html.Div([
        dcc.Graph(figure=fig3),
    ]),
    html.Div([
        html.H1("Comparison plots for CH4, CO2, and CO using Rutgers and ASRC data",
                style={'text-align':'center', 'font-size':'48px'}),
        dcc.Graph(figure=fig4),
    ])

])

if __name__ == '__main__':
    app.run_server(debug=False)

#app.run_server(host='0.0.0.0', debug=True, use_reloader=False)
