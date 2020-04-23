import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_design_kit as ddk
import pandas as pd
import os
import dash_bootstrap_components as dbc
from app import dash_app

main_path_data = os.path.abspath("./data")
# all_cardsBD = pd.read_csv(main_path_data + '\\news.csv')

if os.path.isfile(main_path_data + '\\news.csv'):
    all_cardsBD = pd.read_csv(main_path_data + '\\news.csv')
    pass
else:
    # serverBD = pd.read_csv(StringIO(s.decode('utf-8')))
    all_cardsBD = pd.read_csv('https://raw.githubusercontent.com/Slavian2015/BestKino/master/data/news.csv')

    all_cardsBD.to_csv(main_path_data + '\\news.csv')
    pass


###################   ALL   FILMS    #######################
rows = []

rows.append(html.Tr([html.Td("№", style={'text-align': 'center'}),
                     html.Td("Название", style={'text-align': 'center'}),
                    html.Td("Дата создания", style={'text-align': 'center'}),
                    html.Td("Статус", style={'text-align': 'center'}),
                    html.Td("Редактировать", style={'text-align': 'center'}),
                    html.Td("Удалить", style={'text-align': 'center'})]))
for ind in all_cardsBD.index:
    rows.append(html.Tr([html.Td(ind, style={'text-align': 'center'}),
                     html.Td(all_cardsBD['name'][ind], style={'text-align': 'center', 'max-width':'250px'}),
                    html.Td(all_cardsBD['date'][ind], style={'text-align': 'center','max-width':'82px'}),
                         html.Td(all_cardsBD['status'][ind], style={'text-align': 'center', 'max-width': '82px'}),

                    html.Td(style={'text-align': 'center'}, children=[html.Button("Редактировать", style={'text-align': 'center','max-width': '140px','font-size': '8px'}, n_clicks=0, id={'type':"change_news_btn", 'index':ind})]),
                    html.Td(style={'text-align': 'center'}, children=[html.Button("Удалить", style={'text-align': 'center','max-width': '80px','font-size': '8px'}, n_clicks=0, id={'type':"delet_news_btn", 'index':ind})])]))

table_body = [html.Tbody(rows)]
table = dbc.Table(table_body,
                  bordered=True,
                  dark=True,
                  hover=True,
                  responsive=True,
                  striped=True)


###################   FILMS  CHANGE / NEW  #######################


chenges = ddk.Card(shadow_weight='heavy',
                   style={'background-color': '#14404c', 'color': 'azure', 'padding':'0px'},
                   children=[
ddk.Block(children=[ddk.Block(width=30, children=[html.P("iD новости")]),ddk.Block(width=70, children=[html.H1("337777", id="id_news_tab",)])]),
ddk.Block(children=[ddk.Block(width=30, children=[html.P("Название новости")]),ddk.Block(width=70, children=[dcc.Input(id="name_news_tab", style={'color':'black'},type="text", placeholder=""),])]),
ddk.Block(children=[ddk.Block(width=30, children=[html.P("Описание")]),ddk.Block(width=70, children=[dcc.Textarea(
        id='disc_news_tab',
        placeholder='Textarea content initialized\nwith multiple lines of text',
        style={'width': '100%', 'color':'black','height': 200})])]),
ddk.Block(children=[ddk.Block(width=30, children=[html.P("Ссылка на картинку")]),ddk.Block(width=70, children=[dcc.Input(id="pic_news_tab", style={'color':'black'},type="text", placeholder="http://"),])]),
ddk.Block(children=[ddk.Block(width=30, children=[html.P("Ссылка на видео")]),ddk.Block(width=70, children=[dcc.Input(id="youtube_news_tab", style={'color':'black'},type="text", placeholder="http://"),])]),
ddk.Block(style={'text-align':'center', 'margin-top': '10px'},children=[html.Button("Сохранить",id="save_news_tab",)])])




news_block = ddk.Block(children=[
                            ddk.Block(width=50,
                                      style={'padding': '10px'},
                                      children=[table]),
                            ddk.Block(width=50,
                                      children=[chenges])
])


second_tab = dcc.Tab(label="НОВОСТИ",
                     children=[news_block],
                     style={'margin': '10px',
                            'border-radius': '10px',
                            'background-color': '#0e4e70',
                            'color': 'azure',
                            'border': '1px solid rgb(14, 78, 112)'},
                     selected_style={'margin': '10px',
                                     'border-radius': '10px', 'background-color': '#0e4e70', 'color': 'azure',
                                     'border': '2px solid #1f78b4'})