from dash import dcc, html
import dash_bootstrap_components as dbc

PYT_LOGO = "assets/python4.png"

entry_Info = html.Div([
    html.H1(
        'Dash Enterprise',
        className='center',
        style={'margin': '80px'}
    ),
    html.H2(
        'Dash apps go where traditional BI cannot. NLP, object detection,'
        ' predictive analytics, and more. With 1M+ downloads/month,'
        ' Dash is the new standard for AI & data science apps.',
        className='center'
    ),

])

navbar_layout = html.Div([
    html.Div(
        dbc.Navbar(
            dbc.Container(
                [
                    html.A(
                        dbc.Row(
                            [
                                dbc.Col(html.Img(src=PYT_LOGO, height="70px", style={'borderRadius': '10px'})),
                            ],
                            align="center",
                            className="g-0",
                        ),
                        href="#",
                        style={"textDecoration": "none"},
                        className='container',
                    ),
                    dbc.Col(
                        [
                            html.Div([
                                html.Div(dbc.NavItem(dbc.NavLink("Home",  href="/"))),
                                html.Div(dbc.NavItem(dbc.NavLink("Input", href="/input"))),
                                html.Div(dbc.NavItem(dbc.NavLink("Report", href="/report"))),
                            ], className='space'),

                        ],

                    )

                ],
            ),
            color="#98f9dc",
            dark=True,

        )),
])

input_layout = html.Div([
    navbar_layout,
    html.Div(
        className='center',
        children=[
            html.Div(
                'PYTHON SPECIALIST EXERCISE',
                className="center-margin"
            ),
        ]
    ),
    html.Div([
        html.Div(
            className='center',
            children=[

                dcc.Input(
                    className='input',
                    type='number',
                    id="input-on-submit",
                    style={'borderRadius': '50px', 'height': '55px'},
                    min=1,
                    max=1000,
                    placeholder="Enter value between 0-1001",
                    autoFocus=True,
                ),

                html.Button(
                    'Submit',
                    className='btn-hover',
                    id='submit-val',
                ),
            ]
        )
    ]

    ),
    html.Div(
        id='container-button-basic',
        className='report'
    ),
])

report_layout = html.Div([
    navbar_layout,
    html.H1(
        'Report',
        className='center',
        style={'margin': '80px'}
    ),
])

index_layout = html.Div([
    navbar_layout,
    entry_Info
])