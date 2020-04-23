import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_design_kit as ddk
import uuid
import os
from app import dash_app
import pandas as pd
main_path_data = os.path.abspath("./data")



def news_items():
    newsBD = pd.read_csv(main_path_data + '\\news.csv')
    cards = []


    for ind in newsBD.index:

        cards_items=ddk.Block(width=33,
                              children=[
                                  html.A(href='/{}'.format(str(newsBD['Mid'][ind])),
                                         id={'type': 'news-poster',
                                             'index': str(newsBD['Mid'][ind])},
                                         n_clicks=0,
                                         children=[
                                             ddk.Card(width=100,
                                                      style={'margin-bottom': '40px',
                                                             'background-color': 'rgb(14, 78, 112)',
                                                             'color': 'azure'},
                                                      children=[
                                  ddk.Logo(src=str(newsBD['poster'][ind]),
                                            style={'text-align': 'center',
                                               'max-height': '200px',
                                               'max-width': '-webkit-fill-available',
                                               'height': '200px',
                                               'padding': '0px', 'margin': '0',
                                               'vertical-align': '-webkit-baseline-middle'}),

                                  ddk.Block(width=100,
                                            style={'padding': '0px', 'margin': '2px', },
                                            children=[html.H2(str(newsBD['name'][ind]),
                                                              style={'padding': '0px', 'margin': '0', },)]),
                                  ddk.Block(width=100,
                                            style={'padding': '5px', 'margin': '0',
                                                   'max-height': '200px',
                                                   'overflowY':'hidden' },
                                            children=[html.P(str(newsBD['disc'][ind]),
                                                                  style={'width': '90%','padding': '0px',
                                                                         'margin': '0', },
                                                                  )])
                              ])])])



        cards.append(cards_items)
    return cards


##########################        MAIN PAGE      ##############################
News_main = ddk.Block(width=100,
                        style={'height': '93vh','margin':'0',
                                       'padding':'0',
                         'text-align':'center'},
                        children=[
                            ddk.Block(width=100,
                                      style={'margin': '0', 'padding': '0'},
                                      children=[ddk.Logo(
                                          src='./assets/11.jpg',
                                          style={'text-align': 'center',
                                                 'max-height': '300px',
                                                 "max-width": "-webkit-fill-available",
                                                 'padding': '0px', 'margin': '0',
                                                 'vertical-align': '-webkit-baseline-middle'})]),
                            ddk.Block(width=80,
                                style={'height':'100%', 'margin':'0',
                                       'padding':'0', 'color':'azure',
                                       'overflowY': 'scroll', 'overflowX': 'hidden',
                                       'justify':'center' },
                                children=[
                                    ddk.Block(width=100,
                                              style={'margin':'0','padding':'0'},
                                              children=[ddk.Block(width=100,
                                                                  style={'padding': '0',
                                                                         'margin': '0',},
                                                                  children=[]),
                                                        ddk.Block(width=100,
                                                                  children=[i for i in news_items()])]),

]),

                            ddk.Block(width=20,
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
ddk.Block(width=100,
                                         style={'color':'azure'},
                                         children=[
                                             ddk.Block(width=40,
                                                       children=[
                                                           ddk.Block(width=100,
                                                                     children=[html.H2("Мобильные приложения")]),
                                                           ddk.Block(width=100,
                                                                     children=[ddk.Block(width=50,
                                                                                         children=[ddk.Logo(
                                                                                             style={
                                                                                                 "max-height": "40px",
                                                                                                 "max-width": "180px",
                                                                                                 'margin': '0',
                                                                                                 'padding': '0'},
                                                                                             src='../assets/Android.png')]),
                                                                               ddk.Block(width=50,
                                                                                         children=[ddk.Logo(style={
                                                                                             "max-height": "40px",
                                                                                             "max-width": "180px",
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
                                                                               style={"max-height": "30px",
                                                                                      "max-width": "180px",
                                                                                      'margin-top': '2.2em'},
                                                                               src='../assets/soc.png')]),
                                                                 ])
                                         ])
                        ])


def news_card(id):

    all_newsBD = pd.read_csv(main_path_data + '\\news.csv')
    # id = id.replace("/", "")

    df = all_newsBD[(all_newsBD['Mid'].isin([id]))]

    # df.iloc[0]['youtube']



    ##############     HEAD CARD of MATCH   ###################################


    # ytube = '''<iframe width="875" height="378" src="https://youtu.be/nAXX9eRDg4o" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    #
    # '''




    news_card = ddk.Block(width=100,
                           style={'height':'90vh', 'overflowY':'scroll',
                             'text-align':'center'},
                           children=[
                               ddk.Block(width=100,
                                         style={'margin': '0', 'padding': '0'},
                                         children=[ddk.Logo(
                                             src='./assets/11.jpg',
                                             style={'text-align': 'center',
                                                    'max-height': '300px',
                                                    "max-width": "-webkit-fill-available",
                                                    'padding': '0px', 'margin': '0',
                                                    'vertical-align': '-webkit-baseline-middle'})]),

                               ddk.Block(width=100,
                                         style={'margin-top':"20px", 'padding': '5px', 'color':'azure'},
                                         children=[

                                             ddk.Block(width=80,
                                                       style={},
                                                       children=[ddk.Block(width=30,
                                                                          style={},
                                                                          children=[ddk.Logo(
                                                                                    src=df.iloc[0]['poster'],
                                                                                    style={'text-align': 'center',
                                                               'height': '280px',
                                                               "max-width": "-webkit-fill-available",
                                                               'padding': '0px', 'margin': '0',
                                                             'vertical-align': '-webkit-baseline-middle'})]),

                                                                 ddk.Block(width=70,
                                                                           style={},
                                                                           children=[
                                                                               ddk.Block(width=60,
                                                                           style={},
                                                                           children=[html.H1(df.iloc[0]['name'])]),
                                                                               ddk.Block(width=60,
                                                                           style={},
                                                                           children=[html.P(df.iloc[0]['disc'])]),]),
                                                                 ]),
                                             ddk.Block(width=20,
                                                       style={},
                                                       children=[ddk.Logo(
                                                                                    src='./assets/png/super.png',
                                                                                    style={'text-align': 'center',
                                                               'height': '280px',
                                                               "max-width": "-webkit-fill-available",
                                                               'padding': '0px', 'margin': '0',
                                                             'vertical-align': '-webkit-baseline-middle'})]),
                                         ]),

                               ddk.Block(width=100,
                                         style={'color':'azure'},
                                         children=[
                                             ddk.Block(width=40,
                                                       children=[
                                                           ddk.Block(width=100,
                                                                     children=[html.H2("Мобильные приложения")]),
                                                           ddk.Block(width=100,
                                                                     children=[ddk.Block(width=50,
                                                                                         children=[ddk.Logo(
                                                                                             style={
                                                                                                 "max-height": "40px",
                                                                                                 "max-width": "180px",
                                                                                                 'margin': '0',
                                                                                                 'padding': '0'},
                                                                                             src='../assets/Android.png')]),
                                                                               ddk.Block(width=50,
                                                                                         children=[ddk.Logo(style={
                                                                                             "max-height": "40px",
                                                                                             "max-width": "180px",
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
                                                                               style={"max-height": "30px",
                                                                                      "max-width": "180px",
                                                                                      'margin-top': '2.2em'},
                                                                               src='../assets/soc.png')]),
                                                                 ])
                                         ])




])

    return news_card



