import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_design_kit as ddk
import uuid
import os
from app import dash_app
import pandas as pd
import dash_dangerously_set_inner_html
main_path_data = os.path.abspath("./data")



def film_card(id):

    all_cardsBD = pd.read_csv(main_path_data + '\\server.csv')
    # id = id.replace("/", "")

    df = all_cardsBD[(all_cardsBD['Mid'].isin([id]))]

    # df.iloc[0]['youtube']



    ##############     HEAD CARD of MATCH   ###################################


    # ytube = '''<iframe width="875" height="378" src="https://youtu.be/nAXX9eRDg4o" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    #
    # '''

    row1 = html.Tr([html.Td("год", style={'text-align':'right'}), html.Td(df.iloc[0]['year'])])
    row2 = html.Tr([html.Td("страна",style={'text-align':'right'}), html.Td(df.iloc[0]['country'])])
    row3 = html.Tr([html.Td("жанр",style={'text-align':'right'}), html.Td(df.iloc[0]['ganr'])])
    row4 = html.Tr([html.Td("время",style={'text-align':'right'}), html.Td(df.iloc[0]['time'])])

    table_body = [html.Tbody([row1, row2, row3, row4])]

    table = dbc.Table(table_body,
                      bordered=True,
                      dark=True,
                        hover=True,
                        responsive=True,
                        striped=True,)







    match_card = ddk.Block(width=100,
                           style={'height':'90vh', 'overflowY':'scroll',
                             'text-align':'center'},
                           children=[
                               ddk.Block(width=100,
                                    style={'height':'400px'},
                                    children=[html.Iframe(src='https://youtu.be/nAXX9eRDg4o',
                                                          width="-webkit-fill-available",
                                                          sandbox='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture',
                                                          height="auto",
                                                          style={'frameborder':'0', 'width':"-webkit-fill-available", 'height': 'inherit'})]),

                               ddk.Block(width=100,
                                         style={'margin-top':"20px", 'padding': '5px', 'color':'azure'},
                                         children=[

                                             ddk.Block(width=40,
                                                       style={},
                                                       children=[ddk.Block(width=100,
                                                                          style={},
                                                                          children=[ddk.Logo(
                                                        src=df.iloc[0]['poster'],
                                                        style={'text-align': 'center',
                                                               'height': '280px',
                                                               "max-width": "-webkit-fill-available",
                                                               'padding': '0px', 'margin': '0',
                                                             'vertical-align': '-webkit-baseline-middle'})]),
                                                                 ddk.Block(width=100,
                                                                           style={},
                                                                           children=[table]),
                                                                 ]),
                                             ddk.Block(width=60,
                                                       style={},
                                                       children=[ddk.Block(width=100,
                                                                          style={},
                                                                          children=[html.Button('Купить билет')]),
                                                                 ddk.Block(width=100,
                                                                           style={},
                                                                           children=[html.H1(df.iloc[0]['name'])]),
                                                                 ddk.Block(width=100,
                                                                           style={'padding-left':"20px",'padding-right':"20px",},
                                                                           children=[html.P(df.iloc[0]['disc'])]),
                                                                 ])
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

    return match_card

