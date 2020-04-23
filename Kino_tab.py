import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_design_kit as ddk


kino_block = ddk.Block(children=[
ddk.Block(width=50,
          children=[]),
ddk.Block(width=50,
          children=[])
])






first_tab = dcc.Tab(label="ФИЛЬМЫ",
                    children=[],
                    style={'margin': '10px',
                             'border-radius': '10px',
                             'background-color': '#0e4e70', 'color': 'azure',
                             'border': '1px solid rgb(14, 78, 112)'},
                    selected_style={'margin': '10px', 'border-radius': '10px',
                                    'background-color': '#0e4e70',
                                    'color': 'azure',
                                    'border': '2px solid #1f78b4'})