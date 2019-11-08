import json
from dashboard.apps.failures.failuresTK import *
from dashboard.apps.components.modal import Modal


def layout():
    return html.Div(
        id='failures',
        children=[
            html.Div(
                id='failures-table-container',
                children=[
                    html.Div(id='loading-failures-table', className='loading-page', children="LOADING"),
                ]
            ),
            html.Div(
                id='update-resolution-modal-container',
                children=[
                    Modal(
                        id='update-resolution-modal',
                        title="CHANGE RESOLUTION",
                        children=initial_modal_layout()
                    )
                ],
                style={
                    'display': 'none'
                }
            )
        ]
    )