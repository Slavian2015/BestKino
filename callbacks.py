from dash.dependencies import Input, Output, State, ALL, MATCH
from app import dash_app
import dash
from layouts import admin_tabs
from News_card import news_card
import News_card
from Film_card import film_card
import os
import pandas as pd
import json
import Kino_tab
import News_tab
import layouts
from dash.exceptions import PreventUpdate
from io import StringIO
# import requests


dash_app.config['suppress_callback_exceptions'] = True
main_path_data = os.path.abspath("./data")

# url = 'https://raw.githubusercontent.com/Slavian2015/BestKino/master/data/server.csv'
# url2 = 'https://raw.githubusercontent.com/Slavian2015/BestKino/master/data/news.csv'
# s = requests.get(url).text
# s2 = requests.get(url2).text


def film_BD():
    if os.path.isfile(main_path_data + '\\server.csv'):
        all_cardsBD = pd.read_csv(main_path_data + '\\server.csv')
        return all_cardsBD
    else:
        all_cardsBD = pd.read_csv('https://raw.githubusercontent.com/Slavian2015/BestKino/master/data/server.csv')
        all_cardsBD.to_csv(main_path_data + '\\server.csv')
        return all_cardsBD



def news_BD():
    if os.path.isfile(main_path_data + '\\news.csv'):
        all_newsBD = pd.read_csv(main_path_data + '\\news.csv')
        return all_newsBD
    else:
        all_newsBD = pd.read_csv("https://raw.githubusercontent.com/Slavian2015/BestKino/master/data/news.csv")
        all_newsBD.to_csv(main_path_data + '\\news.csv')
        return all_newsBD




def cardwindow(app: dash.Dash):
    @app.callback(
        Output('page-content', 'children'),
        [Input('url', 'pathname')])
    def display_output(pathname):

        for i in film_BD()['Mid']:
            if pathname == "/{}".format(i):
                return film_card(i)

        for i in news_BD()['Mid']:
            if pathname == "/{}".format(i):
                return news_card(i)

        if pathname == '/news':
            return News_card.news_main()
        elif pathname == '/admin':
            return admin_tabs
        elif pathname == '/':
            return layouts.main_page()
        else:
            return '404'




def new_film(app: dash.Dash):
    @app.callback(
        [Output('id_tab', 'children'),
         Output('name_tab', 'value'),
         Output('disc_tab', 'value'),
         Output('pic_tab', 'value'),
         Output('youtube_tab', 'value')],
        [Input({'type': 'change_btn', 'index': ALL}, 'n_clicks')],
    )
    def display_output(*args):

        ctx = dash.callback_context
        if not ctx.triggered:
            return [],[],[],[],[]

        else:
            button_id = ctx.triggered[0]['prop_id'].split('.')[0]

            res = json.loads(button_id)

            df = film_BD()

            id = df['Mid'][res['index']]
            name = df['name'][res['index']]
            disc = df['disc'][res['index']]
            pic = df['poster'][res['index']]
            you = df['youtube'][res['index']]


            return id, name, disc, pic, you


            ##########   SHOWS   all callbacks info  ###########

        # ctx_msg = json.dumps({
        #     'states': ctx.states,
        #     'triggered': ctx.triggered,
        #     'inputs': ctx.inputs
        # }, indent=2)
        #
        # print("ctx_msg  :", ctx_msg)


def save_film(app: dash.Dash):
    @app.callback(
        Output('film_list', 'children'),
        [Input('save_film_tab', 'n_clicks')],
        [State('id_tab', 'children'),
         State('name_tab', 'value'),
         State('disc_tab', 'value'),
         State('pic_tab', 'value'),
         State('youtube_tab', 'value')],

    )
    def display_output(n_clicks, id, name, disc, pic, you):

        # ctx = dash.callback_context
        # if not ctx.triggered:
        #     print("####  ctx.triggered  ####")
        #     return Kino_tab.film_list()
        #
        # elif ctx.triggered:
        #     button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        #     print("button_id  ctx ", button_id)
        #     res = json.loads(button_id)
        #     print("res ", res)
        #
        #     df = film_BD()
        #     df.drop(res)
        #     df.to_csv(main_path_data + '\\server.csv', index=False)
        #     print("####  DELETED  ####")

        if n_clicks is None:
            raise PreventUpdate

        else:
            df = film_BD()
            filter = df[df['Mid'] == id].index


            df.loc[filter, 'name'] = name
            df.loc[filter, 'disc'] = disc
            df.loc[filter, 'poster'] = pic
            df.loc[filter, 'youtube'] = you
            df.to_csv(main_path_data + '\\server.csv', index=False)
            print("####  SAVED  ####")

            return Kino_tab.film_list()


def new_news(app: dash.Dash):
    @app.callback(
        [Output('id_news_tab', 'children'),
         Output('name_news_tab', 'value'),
         Output('disc_news_tab', 'value'),
         Output('pic_news_tab', 'value')
         ],
        [Input({'type': 'change_news_btn', 'index': ALL}, 'n_clicks')],
    )
    def display_output(*args):

        ctx = dash.callback_context
        if not ctx.triggered:
            return [],[],[],[]

        else:
            button_id = ctx.triggered[0]['prop_id'].split('.')[0]
            res = json.loads(button_id)

            df = news_BD()

            id = df['Mid'][res['index']]
            name = df['name'][res['index']]
            disc = df['disc'][res['index']]
            pic = df['poster'][res['index']]



            return id, name, disc, pic


            ##########   SHOWS   all callbacks info  ###########

        # ctx_msg = json.dumps({
        #     'states': ctx.states,
        #     'triggered': ctx.triggered,
        #     'inputs': ctx.inputs
        # }, indent=2)
        #
        # print("ctx_msg  :", ctx_msg)


def save_news(app: dash.Dash):
    @app.callback(
        Output('news_list', 'children'),
        [Input('save_news_tab', 'n_clicks')],
        [State('id_news_tab', 'children'),
         State('name_news_tab', 'value'),
         State('disc_news_tab', 'value'),
         State('pic_news_tab', 'value'),
         ],

    )
    def display_output(n_clicks, id, name, disc, pic):

        # ctx = dash.callback_context
        # if not ctx.triggered:
        #     print("####  ctx.triggered  ####")
        #     return Kino_tab.film_list()
        #
        # elif ctx.triggered:
        #     button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        #     print("button_id  ctx ", button_id)
        #     res = json.loads(button_id)
        #     print("res ", res)
        #
        #     df = film_BD()
        #     df.drop(res)
        #     df.to_csv(main_path_data + '\\server.csv', index=False)
        #     print("####  DELETED  ####")

        if n_clicks is None:
            raise PreventUpdate

        else:
            df = news_BD()
            filter = df[df['Mid'] == id].index


            df.loc[filter, 'name'] = name
            df.loc[filter, 'disc'] = disc
            df.loc[filter, 'poster'] = pic
            df.to_csv(main_path_data + '\\news.csv', index=False)
            print("####  SAVED   news  ####")

            return News_tab.news_list()



cardwindow(dash_app)
new_film(dash_app)
save_film(dash_app)
new_news(dash_app)
save_news(dash_app)