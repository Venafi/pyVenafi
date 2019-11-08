from dashboard.apps.views.viewsTK import *
from datetime import datetime
from dashboard.apps.components.modal import Modal


def layout():
    return html.Div(
        id='views',
        children=[
            html.Div(
                id="views-body",
                children=[
                    html.Div(
                        id='filters-container',
                        children=[
                            html.Div(
                                id='filter-selections-container',
                                children=[
                                    get_test_info_filter('test-info-filter'),
                                    get_test_history_filter('test-history-filter'),
                                    get_job_info_filter('job-info-filter'),
                                    get_jobs_history_filter('job-history-filter'),
                                    get_frameworks_filter('framework-filter'),
                                    html.Div(
                                        id='generate-view-container',
                                        children=[
                                            html.Button(
                                                id='generate-view-btn',
                                                className='std-btn',
                                                children="Generate View",
                                                n_clicks=0
                                            )
                                        ]
                                    )
                                ]
                            ),
                            html.Div(
                                id='inverted-filter-collapsible-container',
                                children=[
                                    html.Button(
                                        id='inverted-filter-collapsible-btn',
                                        n_clicks=0
                                    )
                                ]
                            ),
                        ]
                    ),
                    html.Div(
                        id='manage-results-container',
                        children=dcc.Loading(
                            id='loading-output-container',
                            type='circle',
                            children=[html.Div(id='output-container')],
                            style={
                                'display': 'flex',
                                'align-items': 'center',
                                'width': '100%',
                                'background': 'rgba(212, 212, 212, 0.2)',
                                'height': '600px',
                            },
                        ),
                    ),
                    html.Div(
                        id='select-range-modal',
                        children=[
                            Modal(
                                id='range-modal',
                                title="SELECT RANGE",
                                children=[
                                    dcc.DatePickerRange(
                                        id='select-range-date-picker',
                                        start_date=(datetime.today()).strftime('%Y-%m-%d'),
                                        end_date=(datetime.today()).strftime('%Y-%m-%d'),
                                        display_format='MMM D, YYYY',
                                        day_size=45
                                    ),
                                    html.P(
                                        id='date-prompt-in-modal',
                                        children="For every test or job in this date range:"
                                    ),
                                    dcc.RadioItems(
                                        id='select-range-type',
                                        options=[
                                            {'label': 'Return only the latest record', 'value': 'latest-record-only'},
                                            {'label': 'Return every record', 'value': 'every-record'}
                                        ],
                                        value='latest-record-only'
                                    ),
                                    html.Button(
                                        id='go-btn',
                                        className='modal-submit-btn',
                                        children="GO",
                                        n_clicks=0
                                    )
                                ]
                            )
                        ],
                        style={
                            'display': 'none'
                        }
                    )
                ]
            )
        ]
    )
