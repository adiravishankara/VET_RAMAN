from dash import Dash, html, dcc, Input, Output, dash_table
import sys

from backend import Backend

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div([
    html.H2('Peak Detection Optimization'),
    html.Div([
        html.Button(id='load-file', n_clicks=0, children='Load File'),
        html.Img(id='file-loaded', src='../../assets/file_loaded.png', hidden=True, width=55, height=55,
                 style={'padding-left': '20px'})],
        style={'display': 'inline-block'}),
    html.Div([
        dcc.Loading(dcc.Graph(id='graph', ), type='circle'),
        html.Div([
            dash_table.DataTable(id='data-table', style_table={'width': '300px', 'height': '400px', 'overflowY': 'scroll'}),
            html.Div([
                html.Button(id='previous', n_clicks=0, children='Previous'),
                html.Button(id='next', n_clicks=0, children='Next')
            ], style={'display': 'inline-block'}),
        html.Div([
            dash_table.DataTable(id='data-table', style_table={'width': '300px', 'height': '300px', 'overflowY': 'scroll'}),
            dcc.Slider(0, 50, 1, value=0, id='row-slider'),
            html.Button(id='set-data', n_clicks=0, children='Set Data')
        ], id='table', style={}),
        ])
    ])
])

@app.callback(
    Output('')
)


if __name__ == '__main__':
    app.run_server(debug=True)