import dash_html_components as html


def layout():
    return html.Div(
        id='header',
        children=[
            html.H1(
                id="venafi-testing",
                children=[
                    html.A(
                        id='venafi-testing-lnk',
                        children="VENAFI TESTING",
                        href='/'
                    )
                ]
            )
        ]
    )
