from dash.dependencies import Input, Output, State, ALL, MATCH
from app import dash_app
import dash
from layouts import layout_main
from News_card import News_main, news_card
from Film_card import film_card
import os
import pandas as pd
import layouts
from dash.exceptions import PreventUpdate
dash_app.config['suppress_callback_exceptions'] = True
main_path_data = os.path.abspath("./data")

def cardwindow(app: dash.Dash):
    @app.callback(
        Output('page-content', 'children'),
        [Input('url', 'pathname')],
        # [State({'type': 'dynamic-poster', 'index': MATCH}, 'id'),
        #  State({'type': 'dynamic-poster', 'index': MATCH}, 'n_clicks')]
    )

    def display_output(pathname):

        all_cardsBD = pd.read_csv(main_path_data + '\\server.csv')
        for i in all_cardsBD['Mid']:
            if pathname == "/{}".format(i):
                return film_card(i)

        all_newsBD = pd.read_csv(main_path_data + '\\news.csv')
        for i in all_newsBD['Mid']:
            if pathname == "/{}".format(i):
                return news_card(i)

        if pathname == '/news':
            return News_main
        elif pathname == '/all_matches':
            return layout_main
        elif pathname == '/':
            return layout_main
        else:
            return '404'

# def refresh(app: dash.Dash):
#
#     ###############################    RESTART ALL FUNCTIONS     ########################################
#     @app.callback(Output('table-container', 'children'), [Input('interval', 'n_intervals')])
#     def trigger_by_modify(n):
#
#         PARSER.new_refresh()
#         Structure.refresh_BD()
#
#         print("###############  UPDATE   #########################")
#         return

cardwindow(dash_app)
# refresh(dash_app)