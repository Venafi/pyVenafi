import dash_html_components as html
import dash_core_components as dcc


def Modal(id, children, title=''):
    return html.Div(
        className='modal-container',
        children=[
            html.Div(
                className='disable-background'
            ),
            html.Div(
                id=id,
                className='modal',
                children=[
                    html.Div(
                        className='modal-header',
                        children=[
                            html.Span(
                                className='modal-title',
                                children=title
                            ),
                            html.Button(
                                id='%s-close-modal'%id,
                                className='modal-close-btn',
                                n_clicks=0
                            )
                        ]
                    ),
                    dcc.Loading(
                        id='loading-modal-body',
                        children=[
                            html.Div(
                                id='%s-modal-body'%id,
                                className='modal-body',
                                children=children
                            )
                        ],
                        type='circle'
                    )
                ],
                style={
                    'pointer-events': 'all'
                }
            )
        ]
    )