import requests
import json

# Import Dash Modules
from dash import Dash
import dash_html_components as html
from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate

from dashboard.apps.failures import failuresTK as ftk
from dashboard.apps.failures.failuresTK import States
from dashboard.apps.shared import sharedTK as stk
from dashboard import config


def register_failures_callbacks(app):
    assert isinstance(app, Dash)

    @app.callback(
        output=Output('failures-table-container', 'children'),
        inputs=[
            Input('url', 'href')
        ]
    )
    def show_failure_table(href):
        if href:
            return ftk.create_failures_table_container()
        raise PreventUpdate()

    @app.callback(
        output=Output('failures', 'style'),
        inputs=[
            Input('update-resolution-btn', 'n_clicks_timestamp'),
            Input('submit-resolution-btn', 'n_clicks_timestamp'),
            Input('update-resolution-modal-close-modal', 'n_clicks_timestamp')
        ],
        state=[
            State('failures-data-table', 'derived_virtual_selected_rows')
        ]
    )
    def disable_background_of_modal(update_resolution, submit_resolution, close_modal, selected_rows):
        if any(selected_rows):
            return stk.disable_background_of_modal(btns_that_open_modal=[update_resolution], btns_that_close_modal=[submit_resolution, close_modal])
        else:
            return {'pointer-events': 'all'}

    @app.callback(
        output=Output('update-resolution-modal-container', 'style'),
        inputs=[
            Input('update-resolution-btn', 'n_clicks_timestamp'),
            Input('submit-resolution-btn', 'n_clicks_timestamp'),
            Input('update-resolution-modal-close-modal', 'n_clicks_timestamp')
        ],
        state=[
            State('failures-data-table', 'derived_virtual_selected_rows')
        ]
    )
    def hide_or_show_update_resolution_modal(update_resolution, submit_resolution, close_modal, selected_rows):
        max_val = max([btn for btn in [update_resolution, submit_resolution, close_modal] if btn is not None]) if selected_rows else None
        return {'display': 'block' if max_val and max_val == update_resolution else 'none'}

    @app.callback(
        output=Output('warning-banner', 'children'),
        inputs=[
            Input('update-resolution-btn', 'n_clicks_timestamp'),
            Input('submit-resolution-btn', 'n_clicks_timestamp'),
            Input('failures-states', 'children')
        ],
        state=[
            State('failures-data-table', 'derived_virtual_selected_rows'),
        ]
    )
    def update_resolutions_are_rows_selected_check(update_resolution_btn, submit_resolution_btn, state, selected_rows):
        if not (update_resolution_btn or submit_resolution_btn):
            raise PreventUpdate()

        max_val = max([btn for btn in [update_resolution_btn, submit_resolution_btn] if btn is not None])

        if update_resolution_btn == max_val and not selected_rows:
            return html.P("Must select tests to update!", style={'display': 'inline-block', 'color': 'red'})

        elif max_val == submit_resolution_btn:
            state = json.loads(state)
            resolution_state = state.get(States.Resolution.name)
            if resolution_state == States.Resolution.successful:
                msg = "Resolution successfully updated!"
            elif resolution_state == States.Resolution.unsuccessful:
                msg = "ERROR: Resolution could not be updated for the selected tests."
            else:
                msg = ""

            return html.P(
                id='resolution-info-updated',
                children=msg,
                style={
                    'color': '#A33',
                    'whiteSpace': 'normal',
                    'margin-top': '50px',
                    'textAlign': 'center'
                }
        )
        else:
            return ""

    @app.callback(
        output=Output('failures-states', 'children'),
        inputs=[
            Input('update-resolution-modal-close-modal', 'n_clicks_timestamp'),
            Input('submit-resolution-btn', 'n_clicks_timestamp')
        ],
        state=[
            State('resolution-dropdown', 'value'),
            State('failures-data-table', 'derived_viewport_selected_rows'),
            State('failures-data-table', 'derived_viewport_data'),
            State('failures-states', 'children')
        ]
    )
    def update_resolutions(close_modal_btn, submit_resolution_btn, new_resolution, selected_rows, rows, state):
        if not (close_modal_btn or submit_resolution_btn):
            raise PreventUpdate()

        max_val = max([btn for btn in [close_modal_btn, submit_resolution_btn] if btn is not None])
        state = json.loads(state)

        if max_val == submit_resolution_btn:
            try:
                row_values = [rows[i] for i in selected_rows]
                data = {
                    'testIds': [rv['testhistory:testid'] for rv in row_values],
                    'runIds': [rv['testhistory:runid'] for rv in row_values],
                    'resolution': new_resolution
                }

                resp = requests.post(config.API_URL + '/testHistory', data=json.dumps(data))
                successful = resp.status_code == 200
            except:
                successful = False

            resolution_state = state.get(States.Resolution.name)
            if resolution_state is None:
                state[States.Resolution.name] = States.Resolution.not_submitted

            state[States.Resolution.name] = States.Resolution.successful if successful else States.Resolution.unsuccessful

        elif max_val == close_modal_btn:
            state[States.Resolution.name] = States.Resolution.not_submitted

        return json.dumps(state)

    @app.callback(
        output=Output('failures-data-table', 'data'),
        inputs=[
            Input('failures-states', 'children'),
        ],
        state=[
            State('resolution-dropdown', 'value'),
            State('failures-data-table', 'selected_rows'),
            State('failures-data-table', 'data')
        ]
    )
    def update_table_if_resolution_changed(state, new_resolution, selected_rows, rows):
        state = json.loads(state)
        resolution_state = state.get(States.Resolution.name)
        if resolution_state is None or resolution_state != States.Resolution.successful or not selected_rows:
            raise PreventUpdate()

        for row in selected_rows:
            rows[row]['testhistory:resolution'] = new_resolution

        return rows

    @app.callback(
        output=Output('failures-table', 'children'),
        inputs=[
            Input('refresh-failures-table-btn', 'n_clicks')
        ]
    )
    def refresh_data_table(refresh):
        if refresh:
            return ftk.create_failures_table()
        raise PreventUpdate()

    @app.callback(
        output=Output('failures-data-table', 'selected_rows'),
        inputs=[
            Input('failures-states', 'children'),
            Input('select-all-failures-btn', 'n_clicks_timestamp'),
            Input('unselect-all-failures-btn', 'n_clicks_timestamp')
        ],
        state=[
            State('failures-data-table', 'selected_rows'),
            State('failures-data-table', 'derived_virtual_data'),
            State('failures-data-table', 'data'),
        ]
    )
    def update_table_if_resolution_changed(state, select_all_btn, unselect_all_btn, selected_rows, derived_data, all_data):
        state = json.loads(state)
        resolution_state = state.get(States.Resolution.name)
        if resolution_state is None or resolution_state != States.Resolution.successful or not selected_rows:
            select_all = max([btn for btn in [select_all_btn, unselect_all_btn] if btn is not None])
            if not select_all:
                raise PreventUpdate()
            if select_all_btn and int(select_all) == int(select_all_btn):
                derived_tetIds = [x.get('testhistory:testid') for x in derived_data]
                return [i for i, x in enumerate(all_data) if x.get('testhistory:testid') in derived_tetIds]

        return []

    @app.callback(
        output=Output('num-failures-selected', 'children'),
        inputs=[
            Input('failures-data-table', 'selected_rows')
        ]
    )
    def update_row_count_text(selected_rows):
        return "{} rows selected.".format(len(selected_rows) if selected_rows else 0)
