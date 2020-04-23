import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output










second_tab = dcc.Tab(label="НОВОСТИ",
                     children=[],
                     style={'margin': '10px',
                            'border-radius': '10px',
                            'background-color': '#0e4e70',
                            'color': 'azure',
                            'border': '1px solid rgb(14, 78, 112)'},
                     selected_style={'margin': '10px',
                                     'border-radius': '10px', 'background-color': '#0e4e70', 'color': 'azure',
                                     'border': '2px solid #1f78b4'})