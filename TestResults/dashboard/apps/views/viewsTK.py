import dash_html_components as html
import dash_core_components as dcc
import dash_table as dt
from dateutil.parser import parse as parsedt
from dashboard.apps.shared import sharedTK as stk


def arrow(direction, text=''):
    degrees = {
        'up': '-45deg',
        'right': '45deg',
        'down': '135deg',
        'left': '-135deg'
    }
    return html.Div(
        [
            html.Div(
                className='toggle-container',
                children=[
                    html.Span(
                        className='toggle-arrow',
                        style={
                            'transform': 'rotate(%s)' % degrees.get(direction)
                        }
                    )
                ]
            ),
            html.Span(
                className='toggle-text',
                children=text
            )
        ]
    )


def create_filter(id, header, items):
    return html.Div(
        id='%s-container'%id,
        className='filter-container',
        children=[
            html.Button(
                id=id,
                className='toggle-btn',
                children=[arrow(direction='right', text=header)],
                n_clicks=0
            ),
            dcc.Checklist(
                id='%s-items'%id,
                className='toggle-items',
                options=[{'label': i['label'], 'value': i['value']} for i in items],
                style={
                    'display': 'none'
                }
            )
        ]
    )


def get_test_info_filter(id):
    rows = stk.FILTER_DATA['tests']
    return create_filter(id, rows[0]['displayName'], rows[1:])


def get_test_history_filter(id):
    rows = stk.FILTER_DATA['testhistory']
    return create_filter(id, rows[0]['displayName'], rows[1:])


def get_job_info_filter(id):
    rows = stk.FILTER_DATA['jobs']
    return create_filter(id, rows[0]['displayName'], rows[1:])


def get_jobs_history_filter(id):
    rows = stk.FILTER_DATA['jobhistory']
    return create_filter(id, rows[0]['displayName'], rows[1:])

def get_frameworks_filter(id):
    rows = stk.FILTER_DATA['frameworks']
    return create_filter(id, rows[0]['displayName'], rows[1:])


def create_views_table(data, filters):
    """
    :type data: list
    :type filters: list
    :return:
    """
    total_row_count = len(data[1])
    filters += ['frameworks:name']
    if 'testhistory:created' in filters:
        filters += ['runs:created']
    columns = []
    indexes = []
    dateindexes = []

    for index, column in enumerate(data[0]):
        main_header, sub_header = column.lower().split('.')
        column_id = main_header+":"+sub_header
        if column_id not in filters:
            continue
        if main_header == 'frameworks':
            mh = 'Framework'
            sh = 'Type'
        else:
            if main_header == 'runs':
                main_header = 'testhistory'
                sub_header = 'created'
                column_id = 'testhistory:created'
            mh = stk.FILTER_DATA[main_header][0]['displayName']
            sh = [h.get('label') for h in stk.FILTER_DATA[main_header] if h.get('value', '').lower() == sub_header][0]
        column_name = [mh, sh]
        columns.append({"name": column_name,"id": column_id})
        if column in stk.DATELIST:
            dateindexes.append(index)
        indexes.append(index)

    to_dt = lambda x: parsedt(x).strftime('%m-%d-%Y %H:%M')

    rows = [[d[i] if i not in dateindexes else to_dt(d[i]) for i in indexes] for d in data[1]]
    rows = [dict(zip((c['id'] for c in columns), row)) for row in rows]
    rows = [dict(y) for y in set(tuple(x.items()) for x in rows)]

    table = dt.DataTable(
        id='views-data-table',
        columns=sorted(columns, key=lambda x: x['id']),
        merge_duplicate_headers=True,
        data=rows,
        style_header={
            'textAlign': 'center',
            'backgroundColor': 'rgba(127, 127, 127, 0.2)',
        },
        style_cell={
            'textAlign': 'left',
            'minWidth': '200px', 'maxWidth': '200px', 'width': '200px',
            'whiteSpace': 'normal',
            'wordBreak': 'break-all'
        },
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
        export_format='xlsx',
        export_headers='display',
        page_action='native',
        page_size=100,
        fixed_rows={'headers': True},
    )

    return dcc.Loading(
        html.Div(
            id='loading-views-table',
            children=[
                table,
                html.Div(
                    id='views-row-counts-container',
                    children=[
                        html.Span(
                            id='num-views-rows',
                            children="{} rows returned (not including filters).".format(total_row_count)
                        ),
                    ]
                )
            ],
        ),
        type='circle'
    )