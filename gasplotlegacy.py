# Make sure to pip install all requirements!
from IPython.display import display
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import dash # pip install dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__) # Starting the app

# Manually choosing input file, reading in the data as a csv
input_file = "plot_merge_asrc_rutgers" # Probably want to automate this
data = input_file + ".txt"
df = pd.read_csv(data)

#CH4 plot
fig = px.line(df, x = 'UTC_time', y = ['CH4_ppb_asrc','CH4_ppb_rutgers'], title = '<b>Methane (CH4) in parts per billion over time</b>',
            labels = {
                'UTC_time':'Date and Time (UTC)',
            })

#CO2 plot
fig2 = px.line(df, x = 'UTC_time', y = ['CO2_ppm_asrc','CO2_ppm_rutgers'], title = '<b>Carbon Dioxide (CO2) in parts per million over time</b>',
            labels = {
                'UTC_time':'Date and Time (UTC)',
            })

#CO plot
fig3 = px.line(df, x = 'UTC_time', y = ['CO_ppb_asrc','CO_ppb_rutgers'], title = '<b>Carbon Monoxide (CO) in parts per billion over time</b>',
            labels = {
                'UTC_time':'Date and Time (UTC)',
            })
# Unfortuantely px does not natively support double axis plots
# Therefore this code is a teeny bit longer because use plotly graph objs
# In future maybe plotly locks in and fixes this :(

#CH4 vs CO2
fig4 = make_subplots(specs=[[{"secondary_y": True}]])
fig4.add_trace(
    go.Scatter(x=df['UTC_time'], y=df['CH4_ppb_asrc'],name="<b>CH4 ASRC</b>",
               line=dict(color='purple')),
    secondary_y=False,
)
fig4.add_trace(
    go.Scatter(x=df['UTC_time'], y=df['CH4_ppb_rutgers'],name="<b>CH4 Rutgers</b>",
               line=dict(color='purple')),
    secondary_y=False,
)
fig4.add_trace(
    go.Scatter(x=df['UTC_time'], y=df['CO2_ppm_asrc'],name="<b>CO2 ASRC</b>",
               line=dict(color='orange')),
    secondary_y=True,
)
fig4.add_trace(
    go.Scatter(x=df['UTC_time'], y=df['CO2_ppm_rutgers'],name="<b>CO2 Rutgers</b>",
               line=dict(color='orange')),
    secondary_y=True,
)
fig4.update_layout(
    title_text = "<b>Methane (CH4) and Carbon Dioxide (CO2) over time</b>"
)
fig4.update_xaxes(title_text="Date and Time (UTC)")
fig4.update_yaxes(title_text="<b>CH4 ppb (blue)</b>", secondary_y=False)
fig4.update_yaxes(title_text="<b>CO2 ppm (red)</b>", secondary_y=True)

#CO2 vs CO
fig5 = make_subplots(specs=[[{"secondary_y": True}]])
fig5.add_trace(
    go.Scatter(x=df['UTC_time'], y=df['CO2_ppm_asrc'],name="<b>CO2 ASRC</b>",
               line=dict(color='orange')),
    secondary_y=False,
)
fig5.add_trace(
    go.Scatter(x=df['UTC_time'], y=df['CO2_ppm_rutgers'],name="<b>CO2 Rutgers</b>",
               line=dict(color='orange')),
    secondary_y=False,
)
fig5.add_trace(
    go.Scatter(x=df['UTC_time'], y=df['CO_ppb_asrc'],name="<b>CO ASRC</b>",
               line=dict(color='darkcyan')),
    secondary_y=True,
)
fig5.add_trace(
    go.Scatter(x=df['UTC_time'], y=df['CO_ppb_rutgers'],name="<b>CO Rutgers</b>",
               line=dict(color='darkcyan')),
    secondary_y=True,
)
fig5.update_layout(
    title_text = "<b>Carbon Dioxide (CO2) and Carbon Monoxide (CO) over time</b>"
)
fig5.update_xaxes(title_text="Date and Time (UTC)")
fig5.update_yaxes(title_text="<b>CO2 ppm (blue)</b>", secondary_y=False)
fig5.update_yaxes(title_text="<b>CO ppb (red)</b>", secondary_y=True)

#CO vs CH4
fig6 = make_subplots(specs=[[{"secondary_y": True}]])
fig6.add_trace(
    go.Scatter(x=df['UTC_time'], y=df['CO_ppb_asrc'],name="<b>CO ASRC</b>",
               line=dict(color='darkcyan')),
    secondary_y=False,
)
fig6.add_trace(
    go.Scatter(x=df['UTC_time'], y=df['CO_ppb_rutgers'],name="<b>CO Rutgers</b>",
               line=dict(color='darkcyan')),
    secondary_y=False,
)
fig6.add_trace(
    go.Scatter(x=df['UTC_time'], y=df['CH4_ppb_asrc'],name="<b>CH4 ASRC</b>",
               line=dict(color='purple')),
    secondary_y=True,
)
fig6.add_trace(
    go.Scatter(x=df['UTC_time'], y=df['CH4_ppb_rutgers'],name="<b>CH4 Rutgers</b>",
               line=dict(color='purple')),
    secondary_y=True,
)
fig6.update_layout(
    title_text = "<b>Carbon Monoxide (CO) and Methane (CH4) over time</b>"
)
fig6.update_xaxes(title_text="Date and Time (UTC)")
fig6.update_yaxes(title_text="<b>CO ppb (blue)</b>", secondary_y=False)
fig6.update_yaxes(title_text="<b>CH4 ppb (red)</b>", secondary_y=True)

# All of the above

fig7 = make_subplots(specs=[[{"secondary_y": True}]])
fig7.add_trace(
    go.Scatter(x=df['UTC_time'], y=df['CO_ppb_asrc'],name="<b>CO ASRC</b>",
               line=dict(color='darkcyan')),
    secondary_y=False,
)
fig7.add_trace(
    go.Scatter(x=df['UTC_time'], y=df['CO_ppb_rutgers'],name="<b>CO Rutgers</b>",
               line=dict(color='darkcyan')),
    secondary_y=False,
)
fig7.add_trace(
    go.Scatter(x=df['UTC_time'], y=df['CH4_ppb_asrc'],name="<b>CH4 ASRC</b>",
               line=dict(color='purple')),
    secondary_y=False,
)
fig7.add_trace(
    go.Scatter(x=df['UTC_time'], y=df['CH4_ppb_rutgers'],name="<b>CH4 Rutgers</b>",
               line=dict(color='purple')),
    secondary_y=False,
)
fig7.add_trace(
    go.Scatter(x=df['UTC_time'], y=df['CO2_ppm_asrc'],name="<b>CO2 ASRC</b>",
               line=dict(color='orange')),
    secondary_y=True,
)
fig7.add_trace(
    go.Scatter(x=df['UTC_time'], y=df['CO2_ppm_rutgers'],name="<b>CO2 Rutgers</b>",
               line=dict(color='orange')),
    secondary_y=True,
)
fig7.update_layout(
    title_text = "<b>CO, CH4, CO2 over time</b>",
)
fig7.update_xaxes(title_text="Date and Time (UTC)")
fig7.update_yaxes(title_text="<b>CH4 and CO ppb</b>", secondary_y=False)
fig7.update_yaxes(title_text="<b>CO2 ppm (orange)</b>", secondary_y=True)

# Correlation plots
# All 3 subplots are part of fig 8
fig8 = make_subplots(rows=1, cols=3, 
                     subplot_titles=('<b>CO ppb vs CH4 ppm</b>', 
                                     '<b>CO ppb vs CO2 ppm</b>', 
                                     '<b>CO2 ppm vs CH4 ppm</b>'))

# CO vs CH4
fig8.add_trace(
    go.Scatter(x=df['CO_ppb_asrc'], y=df['CH4_ppb_asrc'] / 1000,mode="markers",name="<b>CO vs CH4 ASRC</b>"),
               row=1, col=1,
)
fig8.add_trace(
    go.Scatter(x=df['CO_ppb_rutgers'], y=df['CH4_ppb_rutgers'] / 1000,mode="markers",name="<b>CO vs CH4 Rutgers</b>"),
               row=1, col=1
)
# CO vs CO2
fig8.add_trace(
    go.Scatter(x=df['CO_ppb_asrc'], y=df['CO2_ppm_asrc'],mode="markers",name="<b>CO vs CO2 ASRC</b>"),
               row=1, col=2,
)
fig8.add_trace(
    go.Scatter(x=df['CO_ppb_rutgers'], y=df['CO2_ppm_rutgers'],mode="markers",name="<b>CO vs CO2 Rutgers</b>"),
               row=1, col=2,
)
fig8.add_trace(
    go.Scatter(x=df['CO2_ppm_asrc'], y=df['CH4_ppb_asrc'] / 1000,mode="markers",name="<b>C02 vs CH4 ASRC</b>"),
               row=1, col=3,
)
fig8.add_trace(
    go.Scatter(x=df['CO2_ppm_rutgers'], y=df['CH4_ppb_rutgers'] / 1000,mode="markers",name="<b>C02 vs CH4 Rutgers</b>"),
               row=1, col=3,
)
fig8.update_layout(
    title_text = "<b>Correlation Plots for CH4, CO2, CO</b>"
)


# Look into the app.layout formatting

# Font formatting (text size)
fig.update_layout(font=dict(size=20), yaxis_title = 'Methane (CH4) ppb',
                  legend_title_text='Data Source', 
                  xaxis = dict(rangeslider=dict(visible=True)))
                  # Append above line to each fig.update_layout for horizontal scrollbars
fig2.update_layout(font=dict(size=20), yaxis_title = 'Carbon Dioxide (CO2) ppm',
                   legend_title_text='Data Source', 
                   xaxis = dict(rangeslider=dict(visible=True)))
fig3.update_layout(font=dict(size=20), yaxis_title = 'Carbon Monoxide (CO) ppb',
                   legend_title_text='Data Source',
                   xaxis = dict(rangeslider=dict(visible=True)))
fig4.update_layout(font=dict(size=20), xaxis = dict(rangeslider=dict(visible=True)))
fig5.update_layout(font=dict(size=20), xaxis = dict(rangeslider=dict(visible=True)))
fig6.update_layout(font=dict(size=20), xaxis = dict(rangeslider=dict(visible=True)))
fig7.update_layout(font=dict(size=20), xaxis = dict(rangeslider=dict(visible=True)))
fig8.update_layout(font=dict(size=20))

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
        html.H1("Comparison plots for CH4, CO2, and CO using Rutgers and ASRC data.",
                style={'text-align':'center', 'font-size':'48px'}),
        dcc.Graph(figure=fig4),
    ]), 
    html.Div([
        dcc.Graph(figure=fig5),
    ]),   
    html.Div([
        dcc.Graph(figure=fig6),
    ]), 
    html.Div([
        dcc.Graph(figure=fig7),
    ]),
    html.Div([
        dcc.Graph(figure=fig8), 
    ])

])

app.run_server(debug=True, use_reloader=False)