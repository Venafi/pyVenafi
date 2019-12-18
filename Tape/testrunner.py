import re
import os
import unittest
import inspect
import time
import json
import uuid
from typing import *
from datetime import datetime
from tempfile import NamedTemporaryFile
from venafi.tools.logger.config import LOG_DIR, LOG_FILENAME
# from sql.spinDB import TestResults, _insertTestResult
from sql.spinDB import SPIN


GLOBAL_TIMESTAMP = time.strftime('%Y%m%d%H%M')


def get_test_info(test):
    if not isinstance(test, unittest.TestCase):
        return

    file_path = inspect.getfile(test.__class__)
    class_name = test.__class__.__name__
    test_name = test._testMethodName
    errors = []

    try:
        guid = getattr(test.__class__, test_name).guid
    except:
        guid = None
        errors.append(f'Test method {file_path}:{class_name}.{test_name} must have a guid.')

    return {
        'guid': guid,
        'className': class_name,
        'testName': test_name,
        'filePath': file_path,
        'lastRun': datetime.today().isoformat(),
        'errors': errors
    }


def get_test_attributes(test) -> dict:
    errors = []
    try:
        owner = getattr(test.__class__, test._testMethodName).owner
        features = getattr(test.__class__, test._testMethodName).features
    except AttributeError:
        owner = test.__class__.owner
        features = test.__class__.features
    else:
        errors.append('Attributes are not valid.')

    return {
        'owner': owner,
        'features': features,
        'errors': errors
    }


def get_test_results(result, lapse, log_file = None):
    if result.skipped:
        test_result = 'skipped'
    elif len(result.failures) > 0:
        test_result = 'failed'
    else:
        test_result = 'passed'

    return {
        'lapse': lapse,
        'result': test_result,
        'logFile': os.path.split(log_file)[1] if new_logfile else None,
        'runDate': datetime.today().isoformat()
    }


def get_tests_from_suites(suites) -> List[unittest.TestCase]:
    for suite in suites:
        for tests in suite:
            for test in tests:
                yield test


if __name__ == '__main__':
    with NamedTemporaryFile(dir=os.path.dirname(__file__), mode='w', suffix='.json') as temp:
        new_log_dir = f"{LOG_DIR}/{GLOBAL_TIMESTAMP}"
        if not os.path.exists(LOG_DIR):
            os.mkdir(LOG_DIR)
        if not os.path.exists(new_log_dir):
            os.mkdir(new_log_dir)

        stale_logs = [re.search(f"{LOG_FILENAME}.*.(json|html)", filename) for filename in os.listdir(LOG_DIR)]
        for first, second in zip(os.listdir(LOG_DIR), stale_logs):
            path_to_first = os.path.join(LOG_DIR, first)
            if second is not None:
                os.remove(path_to_first)

        loader = unittest.TestLoader()
        start_dir = os.path.abspath(os.path.dirname(__file__))
        print(start_dir)
        suites = loader.discover(start_dir)
        for test in get_tests_from_suites(suites):
            result = unittest.TestResult()
            test_info = get_test_info(test)
            test_attrs = get_test_attributes(test)

            if test_info.get('errors') or test_attrs.get('errors'):
                test._addSkip(result=result, test_case=test, reason=test_info.get('errors'))

            start = time.time()
            test.run(result)
            end = time.time()
            lapse = int(end - start)

            new_logfile = f"{new_log_dir}/{test_info.get('testName')}_{test_info.get('guid')}.html"

            logs = [re.search(f"{LOG_FILENAME}.*.(json|html)", filename) for filename in os.listdir(LOG_DIR)]
            if len(logs) > 0:
                for first, second in zip(os.listdir(LOG_DIR), logs):
                    path_to_first = os.path.join(LOG_DIR, first)
                    if second is not None:
                        if first.endswith('.json'):
                            os.remove(path_to_first)
                        elif first.endswith('.html'):
                            os.rename(path_to_first, new_logfile)
            else:
                new_logfile = None

            test_results = get_test_results(result=result, lapse=lapse, log_file=new_logfile)
            metadata = {
                'testInfo': test_info,
                'testAttributes': test_attrs,
                'testResults': test_results,
            }

            pretty_data = json.dumps(metadata, indent=4)
            temp.write(pretty_data)
            temp.flush()
            # print(pretty_data)
            # print("Here is the test info: {}".format(test_info))
            print('------- Timmy Time ------\n')
            # for crap in test_info:
            #     print("{} has the vaule {}".format(crap, test_info[crap]))
            # for more_crap in test_results:
            #     print("{} has the value {}".format(more_crap, test_results[more_crap]))
            # result_values = list(test_results.values())
            # info_values = list(test_info.values())
            # for crap in info_values:
            #     print('Value {}\n'.format(crap))
            test_id = '600'
            result = '1'
            log_file = 'log_file'
            consec_fail = '0'
            run_date = '2019-12-12 13:41:53.743'
            time_lapse = '3'
            spin = SPIN()

            # _insertTestResult(test_id, result, log_file, consec_fail, run_date, time_lapse)
            # TestResults.insert_results(result_values[1], result_values[2], result_values[3], result_values[4],
            #                            result_values[4], result_values[1])



        print('done')


        #TODO: Throw data from json to DB
        # Archive json file
