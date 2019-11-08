import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from dashboard.app import app
from dashboard.layouts import *       # Layouts
import dashboard.callbacks            # Callbacks -> Do NOT remove this import!
import dashboard.endpoints            # APIs -> Do NOT remove this import!
from dashboard import config


app.layout = html.Div(
    id='all-content',
    children=[
        dcc.Location(id='url', refresh=False),
        html.Div(id='header-content', children=header.layout()),
        html.Div(id='page-content')
    ]
)

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
         return home.layout()
    elif pathname == '/failures':
         return failures.layout()
    elif pathname == '/views':
         return views.layout()
    else:
        return home.layout()


if __name__ == '__main__':
    app.run_server(
        host=config.HOST,
        port=config.PORT,
        debug=config.DEBUG
    )