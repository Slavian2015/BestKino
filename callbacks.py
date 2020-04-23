from dash.dependencies import Input, Output, State, ALL, MATCH
from app import dash_app
import dash
from layouts import layout_main, admin_tabs
from News_card import News_main, news_card
from Film_card import film_card
import os
import pandas as pd
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



def cardwindow(app: dash.Dash):
    @app.callback(
        Output('page-content', 'children'),
        [Input('url', 'pathname')])

    def display_output(pathname):

        if os.path.isfile(main_path_data + '\\server.csv'):
            all_cardsBD = pd.read_csv(main_path_data + '\\server.csv')
            pass
        else:
            all_cardsBD = pd.read_csv('https://raw.githubusercontent.com/Slavian2015/BestKino/master/data/server.csv')
            all_cardsBD.to_csv(main_path_data + '\\server.csv')
            pass

        if os.path.isfile(main_path_data + '\\news.csv'):
            all_newsBD = pd.read_csv(main_path_data + '\\news.csv')
            pass
        else:
            all_newsBD = pd.read_csv("https://raw.githubusercontent.com/Slavian2015/BestKino/master/data/news.csv")
            all_newsBD.to_csv(main_path_data + '\\news.csv')
            pass





        for i in all_cardsBD['Mid']:
            if pathname == "/{}".format(i):
                return film_card(i)

        for i in all_newsBD['Mid']:
            if pathname == "/{}".format(i):
                return news_card(i)

        if pathname == '/news':
            return News_main
        elif pathname == '/admin':
            return admin_tabs
        elif pathname == '/':
            return layout_main
        else:
            return '404'


# def new_film(app: dash.Dash):
#     @app.callback(
#         Output('page-content', 'children'),
#         [Input('url', 'pathname')])


def new_film(app: dash.Dash):
    @app.callback(
        [Output({'type': 'id_tab', 'index': MATCH}, 'children'),
         Output({'type': 'name_tab', 'index': MATCH}, 'value'),
         Output({'type': 'disc_tab', 'index': MATCH}, 'children'),
         Output({'type': 'pic_tab', 'index': MATCH}, 'value'),
         Output({'type': 'youtube_tab', 'index': MATCH}, 'value')],
        [Input({'type': 'change_btn', 'index': MATCH}, 'n_clicks')],
        [State({'type': 'change_btn', 'index': MATCH}, 'id'),
         # State({'type': 'change_btn', 'index': MATCH}, 'value'),
         ]
    )
    def display_output(n_clicks, id):


        # if n_clicks is None:
        #     raise PreventUpdate
        print('############ ', n_clicks)

        print('############ ', id)


        print ('Dropdown222', id['index'])


        # print(('Dropdown333 {}'.format(id[0]["index"])))
        #
        # print(('Dropdown VALUE {}'.format(value)))
        # print(('Dropdown n_clicks {}'.format(n_clicks)))



        return 1,2,3,4,5







cardwindow(dash_app)

new_film(dash_app)