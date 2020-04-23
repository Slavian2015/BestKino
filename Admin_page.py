import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_design_kit as ddk
import uuid
import os
from app import dash_app
import pandas as pd
main_path_data = os.path.abspath("./data")



############################     TABS    ###################################
first_tab = dcc.Tab(label="ФИЛЬМЫ",
                    children=[live_teams,
                            ddk.Block(width=100,
                                      children=html.H2('Team 1', style={'margin': '0px'})),
                            score_table,
                            ddk.Block(width=100,
                                      children=html.H2('Team 2', style={'margin': '0px'})),
                            score_table],
                    style={'margin': '10px',
                         'border-radius': '10px',
                         'background-color': '#0e4e70', 'color': 'azure',
                         'border': '1px solid rgb(14, 78, 112)'},
                    selected_style={'margin': '10px', 'border-radius': '10px',
                                    'background-color': '#0e4e70', 'color': 'azure', 'border': '2px solid #1f78b4'})




second_tab = dcc.Tab(label="НОВОСТИ",
                     children=[stat,chart_table],
                     style={'margin': '10px',
                            'border-radius': '10px',
                            'background-color': '#0e4e70',
                            'color': 'azure',
                            'border': '1px solid rgb(14, 78, 112)'},
                     selected_style={'margin': '10px',
                                     'border-radius': '10px', 'background-color': '#0e4e70', 'color': 'azure',
                                     'border': '2px solid #1f78b4'})



tabs = dcc.Tabs(children=[first_tab, second_tab])





##########################        MAIN PAGE      ##############################
admin_card = ddk.Block(width=100,
                       style={'height': '93vh',
                                         'text-align': 'center'},
                       children=[
                           ddk.Block(width=70,
                                      style={'height': '89vh', 'margin': '0', 'padding': '0', 'color': 'azure', 'overflowY': 'scroll',
                                             'overflowX': 'hidden', },
                                      children=[
                  ddk.Card(style={'width': '-webkit-fill-available', 'margin': '10px', 'padding': '0',
                                  'background-color': '#f9f9f91c', },
                           children=tabs)])])


