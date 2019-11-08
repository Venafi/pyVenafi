import requests
import json

# Import Dash Modules
from dash import Dash
from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate

# Import custom dependencies
import dashboard.apps.views.viewsTK as vtk
from dashboard.apps.shared import sharedTK as stk
from dashboard import config


def register_views_callbacks(app):
    assert isinstance(app, Dash)

    def toggle_display_of_filter_items(btnId, itemsId):
        @app.callback(Output(itemsId, 'style'), [Input(btnId, 'n_clicks')])
        def wrap(clicks):
            return {'display': 'none'} if not int(clicks) % 2 else {'display': 'block'}
        return wrap

    def toggle_arrow_action(btnId, text):
        @app.callback(Output(btnId, 'children'), [Input(btnId, 'n_clicks')])
        def wrap(clicks):
            return vtk.arrow('right', text) if not int(clicks)%2 else vtk.arrow('down', text)
        return wrap

    def adjust_toggle_btn_style(btnId, itemsId):
        @app.callback(Output(btnId, 'style'), [Input(btnId, 'n_clicks'), Input(itemsId, 'value')])
        def wrap(clicks, checked_items):
            borderRadius = '5px' if not int(clicks) % 2 else '5px 5px 0px 0px'
            if checked_items and len(checked_items) > 0:
                color = 'green'
                borderColor = 'green'
                backgroundColor = 'rgba(0, 255, 0, 0.1)'
            else:
                color = '#555'
                borderColor = '#BBB'
                backgroundColor = 'transparent'
            return {
                'border-radius': borderRadius,
                'border-color': borderColor,
                'color': color,
                'background-color': backgroundColor
            }
        return wrap

    def register_filter_callbacks(btnId, text):
        itemsId = btnId + "-items"
        adjust_toggle_btn_style(btnId, itemsId)
        toggle_arrow_action(btnId, text)
        toggle_display_of_filter_items(btnId, itemsId)

    register_filter_callbacks('test-info-filter', 'Test Info')
    register_filter_callbacks('test-history-filter', 'Test History')
    register_filter_callbacks('job-info-filter', 'Job Info')
    register_filter_callbacks('job-history-filter', 'Job History')
    register_filter_callbacks('framework-filter', 'Frameworks')

    @app.callback(
        output=Output('filter-selections-container', 'style'),
        inputs=[
            Input('inverted-filter-collapsible-btn', 'n_clicks')
        ]
    )
    def hide_and_show_filters(clicks):
        display = 'none' if clicks%2 else 'initial'
        return {'display': display}

    @app.callback(
        output=Output('inverted-filter-collapsible-btn', 'children'),
        inputs=[
            Input('inverted-filter-collapsible-btn', 'n_clicks')
        ]
    )
    def toggle_hide_show_filters_arrow(clicks):
        return vtk.arrow('right', "Show Filters") if clicks%2 else vtk.arrow('left', "Hide Filters")

    @app.callback(
        output=Output('inverted-filter-collapsible-btn', 'style'),
        inputs=[
            Input('inverted-filter-collapsible-btn', 'n_clicks')
        ]
    )
    def toggle_hide_show_filters_arrow(clicks):
        border_width = '0px 1px 0px 3px' if clicks%2 else '0px 3px 0px 1px'
        return {'border-width': border_width}

    @app.callback(
        output=Output('select-range-modal', 'style'),
        inputs=[
            Input('generate-view-btn', 'n_clicks_timestamp'),
            Input('go-btn', 'n_clicks_timestamp'),
            Input('range-modal-close-modal', 'n_clicks_timestamp')
        ],
        state=[
            State('test-info-filter-items', 'value'),
            State('test-history-filter-items', 'value'),
            State('job-info-filter-items', 'value'),
            State('job-history-filter-items', 'value'),
        ]
    )
    def show_select_range_modal(generate, go, close, test_info_filter, test_history_filter, job_info_filter, job_history_filter):
        max_val = max([btn for btn in [generate, go, close] if btn is not None])

        if not max_val:
            raise PreventUpdate()

        if max_val == generate:
            if not (test_info_filter or test_history_filter or job_info_filter or job_history_filter):
                return {'display': 'none'}
            return {'display': 'block'}
        elif max_val in (go, close):
            return {'display': 'none'}
        else:
            raise PreventUpdate()

    @app.callback(
        output=Output('views', 'style'),
        inputs=[
            Input('generate-view-btn', 'n_clicks_timestamp'),
            Input('go-btn', 'n_clicks_timestamp'),
            Input('range-modal-close-modal', 'n_clicks_timestamp')
        ],
        state=[
            State('test-info-filter-items', 'value'),
            State('test-history-filter-items', 'value'),
            State('job-info-filter-items', 'value'),
            State('job-history-filter-items', 'value'),
        ]
    )
    def disable_background_of_modal(generate, go, close, *filter_items):
        if any(filter_items):
            return stk.disable_background_of_modal(btns_that_open_modal=[generate], btns_that_close_modal=[go, close])
        else:
            return {'pointer-events': 'all'}

    def _get_all_view(startDate, endDate, frameworks, lastResultOnly,failuresOnly):
        data = {
            'startDate': startDate,
            'endDate': endDate,
            'latestResultOnly': lastResultOnly,
            'failuresOnly': failuresOnly
        }
        if frameworks and len(frameworks) > 0:
            data['frameworkNames'] = frameworks

        resp = requests.get(config.API_URL + '/viewAll', data=json.dumps(data))
        return resp.json() if resp.status_code == 200 else {}

    @app.callback(
        output=Output('output-container', 'children'),
        inputs=[
            Input('generate-view-btn', 'n_clicks_timestamp'),
            Input('go-btn', 'n_clicks_timestamp')
        ],
        state=[
            State('test-info-filter-items', 'value'),
            State('test-history-filter-items', 'value'),
            State('job-info-filter-items', 'value'),
            State('job-history-filter-items', 'value'),
            State('framework-filter-items', 'value'),
            State('select-range-date-picker', 'start_date'),
            State('select-range-date-picker', 'end_date'),
            State('select-range-type', 'value')
        ]
    )
    def create_view(generate, go, test_info, test_history, job_info,
                    job_history, frameworks, start_date, end_date, range_type):

        btn_timestamp = max([btn for btn in [generate, go] if btn is not None])

        if not btn_timestamp:
            raise PreventUpdate()

        desired_data = []
        desired_data += ['tests:'+x.lower() for x in test_info] if test_info else []
        desired_data += ['testhistory:'+x.lower() for x in test_history] if test_history else []
        desired_data += ['jobs:'+x.lower() for x in job_info] if job_info else []
        desired_data += ['jobhistory:'+x.lower() for x in job_history] if job_history else []

        if not desired_data:
            return 'Please select data to display from the filters on the left.'

        if btn_timestamp != go:
            raise PreventUpdate()

        all_data = _get_all_view(
            startDate=start_date,
            endDate=end_date,
            frameworks=frameworks,
            lastResultOnly=range_type and range_type == 'latest-record-only',
            failuresOnly=False
        )

        if not all_data:
            return 'Uh-oh...'

        return vtk.create_views_table(
            data=all_data,
            filters=desired_data
        )
