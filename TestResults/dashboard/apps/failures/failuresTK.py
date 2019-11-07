import dash_html_components as html
import dash_core_components as dcc
import dash_table as dt

import requests
import json
from datetime import datetime, timedelta
from dateutil.parser import parse as parsedt

from dashboard.apps.shared import sharedTK as stk
from dashboard import config


cid = 'column_id'
cwidth = 'column_width'
talign = 'text_align'
CreateHeader = lambda ci, cw, ta: {cid: stk.CreateColumnID(ci), cwidth: cw, talign: ta}

TABLE_HEADERS = [
    # Framework Name
    CreateHeader(stk.FrameworksTable.Columns.name.aliased_name, 100, 'center'),

    # JOB GROUP
    CreateHeader(stk.JobsTable.Columns.name.aliased_name, 150, 'left'),

    # TESTS GROUP
    CreateHeader(stk.TestsTable.Columns.testName.aliased_name, 150, 'left'),
    CreateHeader(stk.TestsTable.Columns.className.aliased_name, 150, 'left'),
    CreateHeader(stk.TestsTable.Columns.lastUpdated.aliased_name, 150, 'left'),

    # TESTHISTORY GROUP
    CreateHeader(stk.TestHistoryTable.Columns.age.aliased_name, 50, 'center'),
    CreateHeader(stk.TestHistoryTable.Columns.reason.aliased_name, 180, 'left'),
    CreateHeader(stk.TestHistoryTable.Columns.resolution.aliased_name, 100, 'left'),

    # HIDDEN
    CreateHeader(stk.TestHistoryTable.Columns.testId.aliased_name, 0, 'unset'),
    CreateHeader(stk.TestHistoryTable.Columns.runId.aliased_name, 0, 'unset'),
]

HIDDEN_TABLE_HEADERS = [
    stk.TestHistoryTable.Columns.testId.aliased_name,
    stk.TestHistoryTable.Columns.runId.aliased_name
]


class States:
    class Resolution:
        name = 'resolution-state'
        not_submitted = 0
        submitted = 1
        successful = 2
        unsuccessful = 3


def get_all_view():
    data = {
        'startDate': (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d'),
        'endDate': (datetime.today()).strftime('%Y-%m-%d'),
        'latestResultOnly': True,
        'failuresOnly': True
    }

    resp = requests.get(config.API_URL + '/viewAll', data=json.dumps(data))
    return resp.json() if resp.status_code == 200 else {}


def create_failures_table():
    data = get_all_view()
    filters = [th[cid] for th in TABLE_HEADERS]
    total_row_count = len(data[1])

    columns = []
    indexes = []
    dateindexes = []

    for index, column in enumerate(data[0]):
        main_header, sub_header = column.lower().split('.')
        column_id = main_header + ":" + sub_header
        if column_id not in filters:
            continue
        if main_header == 'frameworks':
            mh = 'Framework'
            sh = 'Type'
        else:
            mh = main_header.upper()
            sh = sub_header.upper()
        column_name = [mh, sh]
        columns.append({"name": column_name, "id": column_id})
        if column in stk.DATELIST:
            dateindexes.append(index)
        indexes.append(index)

    to_dt = lambda x: parsedt(x).strftime('%m-%d-%Y %H:%M')

    rows = [[d[i] if i not in dateindexes else to_dt(d[i]) for i in indexes] for d in data[1]]
    rows = [dict(zip((c['id'] for c in columns), row)) for row in rows]

    table = dt.DataTable(
        id='failures-data-table',
        columns=sorted(columns, key=lambda x: filters.index(x['id'])),
        merge_duplicate_headers=True,
        data=rows,
        fixed_rows={'headers': True},
        style_header={
            'textAlign': 'center',
            'backgroundColor': 'rgba(127, 127, 127, 0.2)',
        },
        style_cell={
            'whiteSpace': 'normal',
            'wordBreak': 'break-all'
        },
        style_cell_conditional=[
           {
               'if': {'column_id': th[cid]},
               'minWidth': '{w}px', 'maxWidth': '{w}px', 'width': '{w}px'.format(w=th[cwidth]),
               'textAlign': th[talign]
           } for th in TABLE_HEADERS
        ],
        style_table={
            x: '75vh' for x in ['height', 'maxHeight', 'minHeight']
        },
        style_data={
            'padding-left': '10px',
            'padding-right': '10px',
            'fontSize': 'small'
        },
        sort_action='native',
        filter_action='native',
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(248, 248, 248)'
            }
        ],
        row_selectable='multi',
        hidden_columns=[hth.lower().replace('.', ':') for hth in HIDDEN_TABLE_HEADERS],
        page_action='none',
    )

    return table, total_row_count

def create_failures_table_container():
    table, total_row_count = create_failures_table()
    return html.Div(
        id='failure-output-table',
        children=[
            html.Div(
                id='failures-states',
                children=json.dumps({
                    States.Resolution.name: States.Resolution.not_submitted
                }),
                style={
                    'display': 'none'
                }
            ),
            html.Button(
                id='update-resolution-btn',
                className="failures-table-btn",
                children="CHANGE RESOLUTION",
                n_clicks=0
            ),
            html.Button(
                id="select-all-failures-btn",
                className="failures-table-btn",
                children="SELECT ALL",
                n_clicks=0
            ),
            html.Button(
                id="unselect-all-failures-btn",
                className="failures-table-btn",
                children="UNSELECT ALL",
                n_clicks=0
            ),
            html.Button(
                id="refresh-failures-table-btn",
                className="failures-table-btn",
                children="REFRESH TABLE",
                n_clicks=0
            ),
            html.Div(id='warning-banner', style={'display': 'inline-flex', 'margin-left': '12px'}),
            html.Div(id='failures-table', children=table),
            html.Div(
                id='failure-row-counts-container',
                children=[
                    html.Span(
                        id='num-failure-rows',
                        children="{} rows returned.".format(total_row_count)
                    ),
                    html.Span(
                        id='num-failures-selected',
                        children="0 rows selected"
                    )
                ]
            )
        ]
    )

def initial_modal_layout():
    return [
        html.P(
            id='update-resolution-info',
            children="All tests checked in the table with the filters applied to them will be updated to this resolution!",
            style={'color': '#A33', 'whiteSpace': 'normal'}
        ),
        dcc.Dropdown(
            id='resolution-dropdown',
            placeholder="Choose Resolution",
            options=[
                {"label": "Ignored",            "value": "Ignored"},
                {"label": "Product Bug",        "value": "Product Bug"},
                {"label": "Resolved",           "value": "Resolved"},
                {"label": "Under Construction", "value": "Under Construction"},
                {"label": "Undetermined",       "value": "Undetermined"},
            ]
        ),
        html.Button(
            id='submit-resolution-btn',
            className='modal-submit-btn',
            children="SUBMIT",
            n_clicks=0
        )
    ]
