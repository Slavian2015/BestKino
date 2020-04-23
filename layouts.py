import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_design_kit as ddk
import uuid
import os
from app import dash_app
import pandas as pd
main_path_data = os.path.abspath("./data")



def film_items():


    if os.path.isfile(main_path_data + '\\server.csv'):
        serverBD = pd.read_csv(main_path_data + '\\server.csv')
        pass
    else:
        serverBD = pd.read_csv('https://drive.google.com/file/d/1I5QvFQ6fofCQgVwADMYIYpfWEQc6rMgy/view?usp=sharing')
        serverBD.to_csv(main_path_data + '\\server.csv')
        pass

    cards = []


    for ind in serverBD.index:

        cards_items=ddk.Block(width=25,
                              style={'margin-bottom': '40px'},
                              children=[
                                  html.A(href='/{}'.format(str(serverBD['Mid'][ind])),
                                         id={'type': 'dynamic-poster',
                                             'index': str(serverBD['Mid'][ind])},
                                         n_clicks=0,
                                         children=[ddk.Logo(src=str(serverBD['poster'][ind]),
                                                            style={'text-align': 'center',
                                                               'max-height': '-webkit-fill-available',
                                                               'max-width': '-webkit-fill-available',
                                                               'height': '300px',
                                                               'padding': '0px', 'margin': '0',
                                                               'vertical-align': '-webkit-baseline-middle'}),]),

                                  ddk.Block(width=100,
                                            style={'padding': '0px', 'margin': '2px', },
                                            children=[html.H2(str(serverBD['name'][ind]),style={'padding': '0px', 'margin': '0', },)]),
                                  ddk.Block(width=100,
                                            style={'padding': '0px', 'margin': '0', },
                                            children=[html.Button("Купить билет",
                                                                  style={'width': '70%','padding': '0px', 'margin': '0', },
                                                                  id={'type': 'dynamic-cards-btn',
                                                                      'index': str(
                                                                          serverBD['Mid'][ind])},
                                                                  n_clicks=0)])
                              ])



        cards.append(cards_items)
    return cards


##########################        MAIN PAGE      ##############################
layout_main = ddk.Block(width=100,
                        style={'height': '93vh','margin':'0',
                                       'padding':'0',
                         'text-align':'center'},
                        children=[
                            ddk.Block(width=10,
                                style={'height':'100%', 'margin':'0',
                                       'padding':'0', 'color':'azure',
                                       'overflowY': 'scroll', 'overflowX': 'hidden',
                                        'background-image': 'url(/assets/png/bat.png)',
                                                        'background-repeat': 'no-repeat',
                                                        'background-position': 'center',
                                                        # 'background-size': 'auto 130%',
                                                        'background-size': 'cover',
                                       'justify':'center' },
                                children=[]),
                            ddk.Block(width=80,
                                style={'height':'100%', 'margin':'0',
                                       'padding':'0', 'color':'azure',
                                       'overflowY': 'scroll', 'overflowX': 'hidden',
                                       'justify':'center' },
                                children=[


                                    ddk.Block(width=100,
                                              style={'margin':'0','padding':'0'},
                                              children=[ddk.Logo(
                                                        src='./assets/11.jpg',
                                                        style={'text-align': 'center',
                                                               'max-height': '300px',
                                                               "max-width": "-webkit-fill-available",
                                                               'padding': '0px', 'margin': '0',
                                                             'vertical-align': '-webkit-baseline-middle'})]),
                                    ddk.Block(width=100,
                                              style={'margin': '0', 'padding': '0'},
                                              children=[html.H2("Смотрите сегодня, 21.04.2020")]),
                                    ddk.Block(width=100,
                                              style={'margin':'0','padding':'0'},
                                              children=[ddk.Block(width=100,
                                                                  style={'padding': '0',
                                                                         'margin': '0',},
                                                                  children=[]),
                                                        ddk.Block(width=100,
                                                                  children=[i for i in film_items()])]),

                                    ddk.Block(width=100,
                                              style={'margin': '0', 'padding': '0'},
                                              children=[html.H2("Смотрите скоро")]),
                                    ddk.Block(width=100,
                                              style={'margin': '0', 'padding': '0'},
                                              children=[ddk.Block(width=100,
                                                                  style={'padding': '0',
                                                                         'margin': '0', },
                                                                  children=[]),
                                                        ddk.Block(width=100,
                                                                  children=[i for i in film_items()]),

                                    ddk.Block(width=100,
                                              style={'margin': '0', 'padding': '0'},
                                              children=[html.H2("Новости и Акции")]),
                                    ddk.Block(width=100,
                                              style={'margin':'0','padding':'0'},
                                              children=[ddk.Logo(
                                                        src='./assets/11.jpg',
                                                        style={'text-align': 'center',
                                                               'max-height': '300px',
                                                               "max-width": "-webkit-fill-available",
                                                               'padding': '0px', 'margin': '0',
                                                             'vertical-align': '-webkit-baseline-middle'})]),




                                    ddk.Block(width=100,
                                              children=[
                                                  ddk.Block(width=40,
                                                            children=[
                                                                ddk.Block(width=100,
                                                                          children=[html.H2("Мобильные приложения")]),
                                                                ddk.Block(width=100,
                                                                          children=[ddk.Block(width=50,
                                                                                              children=[ddk.Logo(
                                                                                                  style={"max-height":"40px",
                                                                                                         "max-width":"180px",
                                                                                                         'margin': '0',
                                                                                                         'padding': '0'},
                                                                                                  src='../assets/Android.png')]),
                                                                                    ddk.Block(width=50,
                                                                                              children=[ddk.Logo(style={"max-height":"40px",
                                                                                                         "max-width":"180px",
                                                                                                         'margin': '0',
                                                                                                         'padding': '0'},
                                                                                                  src='../assets/aple.png')])])]),
                                                  ddk.Block(width=20,
                                                            children=[ddk.Block(width=100,
                                                                                children=[html.H2("Афиша")]),
                                                                      ddk.Block(width=100,
                                                                                children=[html.P("Расписание")]),
                                                                      ddk.Block(width=100,
                                                                                children=[html.P("Скоро в прокате")]),
                                                                      ddk.Block(width=100,
                                                                                children=[html.P("Кинотеатры")]),
                                                                      ddk.Block(width=100,
                                                                                children=[html.P("Акции")]), ]),
                                                  ddk.Block(width=20,
                                                            children=[ddk.Block(width=100,
                                                                                children=[html.H2("О кинотеатре")]),
                                                                      ddk.Block(width=100,
                                                                                children=[html.P("Новости")]),
                                                                      ddk.Block(width=100,
                                                                                children=[html.P("Реклама")]),
                                                                      ddk.Block(width=100,
                                                                                children=[html.P("Кафе-Бар")]),
                                                                      ddk.Block(width=100,
                                                                                children=[html.P("Контакты")]), ]),
                                                  ddk.Block(width=20,
                                                            children=[ddk.Block(width=100,
                                                                                children=[ddk.Logo(
                                                                                    style={"max-height":"30px",
                                                                                           "max-width":"180px",
                                                                                           'margin-top': '2.2em'},
                                                                                    src='../assets/soc.png')]),
                                                                ])
                                              ])
])]),




                            ddk.Block(width=10,
                                      style={'height': '100%', 'margin': '0',
                                             'padding': '0', 'color': 'azure',
                                             'overflowY': 'scroll', 'overflowX': 'hidden',
                                             'background-image': 'url(/assets/png/super.png)',
                                             'background-repeat': 'no-repeat',
                                             'background-position': 'center',
                                             # 'background-size': 'auto 130%',
                                             'background-size': 'cover',
                                             'justify': 'center'},
                                      children=[]),
])


