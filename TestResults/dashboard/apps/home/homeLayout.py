import dash_html_components as html


def layout():
    return html.Div(
        id='home',
        children=[
            html.Div(
                id="home-body",
                children=[
                    html.Div(
                        id='page-redirect-options',
                        children=[
                            html.A(
                                id='test-failures-lnk',
                                className='btn-lnk',
                                children=[
                                    html.Button(
                                        id='test-failures-btn',
                                        className='large-btn',
                                        children="TEST FAILURES",
                                        n_clicks=0
                                    )
                                ],
                                href='/failures'
                            ),
                            html.A(
                                id='views-lnk',
                                className='btn-lnk',
                                children=[
                                    html.Button(
                                        id='views-btn',
                                        className='large-btn',
                                        children="VIEWS",
                                        n_clicks=0
                                    )
                                ],
                                href='/views'
                            ),
                        ]
                    )
                ]
            )
        ]
    )

