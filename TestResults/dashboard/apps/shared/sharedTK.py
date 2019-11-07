from toolkit.sqlTools import venafiTesting as VT

FrameworksTable = VT.Frameworks()
JobsTable = VT.Jobs()
TestsTable = VT.Tests()
TestHistoryTable = VT.TestHistory()
JobHistoryTable = VT.JobHistory()
RunsTable = VT.Runs()

CreateColumnID = lambda x: x.lower().replace('.', ':')

DATELIST = [
    TestsTable.Columns.lastUpdated.aliased_name,
    JobsTable.Columns.lastUpdated.aliased_name,
    TestsTable.Columns.created.aliased_name,
    JobsTable.Columns.created.aliased_name,
    RunsTable.Columns.created.aliased_name,
]

FILTER_DATA = {
    'testhistory': [
        {'tableName': 'TestHistory' , 'displayName': 'Test History'},
        {'label': 'Run Date'        , 'value': 'created'},
        {'label': 'Test Result'     , 'value': 'testResult'},
        {'label': 'Age'             , 'value': 'age'},
        {'label': 'Failure Reason'  , 'value': 'reason'},
        {'label': 'Resolution'      , 'value': 'resolution'},
        {'label': 'Lapse'           , 'value': 'lapse'}
    ],
    'tests': [
        {'tableName': 'Tests'   , 'displayName': 'Test Info'},
        {'label': 'Class Name'  , 'value': 'className'},
        {'label': 'Test Name'   , 'value': 'testName'},
        {'label': 'Feature'     , 'value': 'feature'},
        {'label': 'Owner'       , 'value': 'owner'},
        {'label': 'Created'     , 'value': 'created'},
        {'label': 'Last Updated', 'value': 'lastUpdated'}
    ],
    'jobs': [
        {'tableName': 'Jobs'            , 'displayName': 'Job Info'},
        {'label': 'Name'                , 'value': 'name'},
        {'label': 'Created'             , 'value': 'created'},
        {'label': 'Last Updated'        , 'value': 'lastUpdated'},
        {'label': 'Last Build Number'   , 'value': 'lastBuildNo'}
    ],
    'jobhistory': [
        {'tableName': 'JobHistory'  , 'displayName': 'Job History'},
        {'label': 'Build Number'    , 'value': 'buildNo'},
        {'label': 'TPP Build'       , 'value': 'build'},
        {'label': 'Release Version' , 'value': 'releaseVersion'},
        {'label': 'Git Branch'      , 'value': 'gitBranch'},
        {'label': 'Total Tests'     , 'value': 'totalTests'},
        {'label': '# Tests Passed'  , 'value': 'passed'},
        {'label': '# Tests Failed'  , 'value': 'failed'},
        {'label': '# Tests Skipped' , 'value': 'skipped'},
        {'label': 'Lapse'           , 'value': 'lapse'},
    ],
    'frameworks': [
        {'tableName': 'Frameworks'  , 'displayName': 'Framework'},
        {'label': 'Python',         'value': 'Python'},
        {'label': 'Integration',    'value': 'Integration'}
    ],
    'runs': [
        {'tableName': 'Runs', 'displayName': 'Runs'},
        {'label': 'Run ID'  , 'value': 'runId'},
        {'label': 'Created' , 'value': 'created'}
    ]
}

def disable_background_of_modal(btns_that_open_modal, btns_that_close_modal):
    max_val = max(btns_that_open_modal + btns_that_close_modal)
    return {'pointer-events': 'none' if max_val and max_val in btns_that_open_modal else 'all'}

