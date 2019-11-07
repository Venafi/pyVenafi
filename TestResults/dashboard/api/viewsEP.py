import json

from toolkit.dashboard.tools import *
from flask import jsonify, request


def register_apis(app):
    def get_request(r, is_bool=False):
        req = {}
        if r in request.args.keys():
            req = request.args.get(r)
        elif request.data:
            data = json.loads(request.data)
            if r in data.keys():
                req = data.get(r)

        if is_bool is True and not isinstance(req, bool):
            try:
                req = bool(req)
            except:
                raise ValueError('Expected a boolean value, but got %s instead.' % str(req))

        return req

    @app.server.route('/api/frameworks', methods=['GET'])
    def get_frameworks_api():
        names = get_request('frameworkNames')
        ids = get_frameworks(names)
        return jsonify(ids)

    @app.server.route('/api/jobs', methods=['GET'])
    def get_jobs_api():
        frameworkIds = get_request('frameworkIds')
        ids = get_jobs(frameworkIds)
        return jsonify(ids)

    @app.server.route('/api/tests', methods=['GET'])
    def get_tests_api():
        jobIds = get_request('jobIds')
        ids = get_tests(jobIds)
        return jsonify(ids)

    @app.server.route('/api/runs', methods=['GET'])
    def get_runs_api():
        startDate = get_request('startDate')
        endDate = get_request('endDate')
        ids = get_runs(startDate, endDate)
        return jsonify(ids)

    @app.server.route('/api/jobHistory', methods=['GET'])
    def get_job_history_api():
        jobIds = get_request('jobIds')
        runIds = get_request('runIds')
        ids = get_job_history(jobIds, runIds)
        return jsonify(ids)

    @app.server.route('/api/testHistory', methods=['GET', 'POST'])
    def get_test_history_api():
        testIds = get_request('testIds')
        runIds = get_request('runIds')
        resolution = get_request('resolution')
        if request.method == 'GET':
            ids = get_test_history(testIds, runIds)
            return jsonify(ids)
        elif request.method == 'POST':
            result = update_test_history_resolution(testIds=testIds, runIds=runIds,
                                           resolution=resolution)
            return jsonify({'Result': result})

    @app.server.route('/api/viewAll', methods=['GET'])
    def get_all_views_api():
        frameworkNames = get_request('frameworkNames')
        startDate = get_request('startDate')
        endDate = get_request('endDate')
        latestResultOnly = get_request('latestResultOnly', is_bool=True)
        failuresOnly = get_request('failuresOnly', is_bool=True)
        data = get_all_view(startDate, endDate, frameworkNames, latestResultOnly, failuresOnly)
        return jsonify(data)
