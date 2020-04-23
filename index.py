from app import dash_app, app
import dash_core_components as dcc
import dash_html_components as html
import dash_design_kit as ddk

import callbacks

# git push heroku master
# https://dash-gallery.plotly.host/Docs/packages/dash-design-kit/dash_design_kit-1.4.0.tar.gz
# --extra-index-url=https://dash-gallery.plotly.host/Docs/packages
# dash-design-kit==1.4.0
# heroku logs --tail



dash_app.scripts.config.serve_locally = True
dash_app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    ddk.App(style={'background-color': 'transparent'},
            children=[ddk.Header(style={'height': '7vh', "margin":"0", 'background-color': '#0e4e70', 'opacity': '1'},
                                 children=[
                                        ddk.Logo(src='../assets/logo.png'),
                                        ddk.Block(style={'text-align': 'right'}, children=[
                                            dcc.Link('Главная', style={'color': 'azure', 'margin': '10px'}, href='/'),

                                            dcc.Link('Новости', style={'color': '#fff', 'margin': '10px'}, href='/news'),
dcc.Link('АДМИНКА', style={'color': '#fff', 'margin': '10px'}, href='/admin'),
                                        ])]),






    html.Div(id='page-content'),
    html.Div(id='table-container'),
    dcc.Interval(id='interval', interval=60000, n_intervals=0),



])])



if __name__ == "__main__":
    # app.run_server(debug=True)
    app.run(debug=False)