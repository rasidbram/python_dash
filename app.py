from dash import Dash, dcc, html, Input, Output, callback, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate

from layouts import index_layout, input_layout, report_layout

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', dbc.themes.BOOTSTRAP]
app = Dash(__name__, update_title=None, title='Py_Spec_Ex', external_stylesheets=external_stylesheets,
           suppress_callback_exceptions=True)

url_bar_and_content_div = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
])

# index layout
app.layout = url_bar_and_content_div


# Index callbacks
@callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/input':
        return input_layout
    elif pathname == '/report':
        return report_layout
    else:
        return index_layout


# input page callbacks
@callback(
    Output('container-button-basic', 'children'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value')
)
def update_output(n_clicks, value):
    if n_clicks is None:
        raise PreventUpdate
    else:
        return f'The all-important value driving our business decisions is {(value + 5)}'


if __name__ == '__main__':
    app.run_server(debug=True)
