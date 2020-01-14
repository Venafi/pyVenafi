import re
import os
import unittest
import inspect
import time
import json
import ftplib
import uuid

from typing import *
from datetime import datetime
from tempfile import NamedTemporaryFile
from venafi.logger import logger
from venafi.tools.logger.logger import LOG_DIR, LOG_FILENAME
from sql.spinDB import SPIN
from pathlib import Path

GLOBAL_TIMESTAMP = time.strftime('%Y%m%d%H%M')


class TestMetaData:
    def __init__(self, metadata):
        self.guid = metadata['testInfo']['guid']
        self.class_name = metadata['testInfo']['className']
        self.test_name = metadata['testInfo']['testName']
        self.file_path = metadata['testInfo']['filePath']
        self.last_run = datetime.fromisoformat(metadata['testInfo']['lastRun'])
        self.test_info_errors = metadata['testInfo']['errors']
        self.owner = metadata['testAttributes']['owner']
        self.features = metadata['testAttributes']['features']
        self.annotation_errors = metadata['testAttributes']['errors']
        self.lapse = metadata['testResults']['lapse']
        self.result = metadata['testResults']['result']
        self.log_file = metadata['testResults']['logFile']
        self.run_date = datetime.fromisoformat(metadata['testResults']['runDate'])


class FTPServer:
    def __init__(self, ftp_server):
        self.server = ftp_server['192.168.7.148']
        self.username = ftp_server['yoda']
        self.password = ftp_server['passw0rd']

    @staticmethod
    def send_file(test_html: str):
        session = ftplib.FTP(host='192.168.7.148', user='yoda', passwd='passw0rd')
        # We need to change to the correct directory, if it's not there, create it
        # check to see if we can get into the directory first
        today = datetime.now()
        if (str(today.year)) in session.nlst():
            session.cwd(str(today.year))
        else:
            session.mkd(str(today.year))
            session.cwd(str(today.year))

        if (str(today.month)) in session.nlst():
            session.cwd(str(today.month))
        else:
            session.mkd(str(today.month))
            session.cwd(str(today.month))

        if (str(today.day)) in session.nlst():
            session.cwd(str(today.day))
        else:
            session.mkd(str(today.day))
            session.cwd(str(today.day))

        # push the file
        session.storbinary('STOR '+test_html, open(test_html, 'rb'))
        session.quit()


def get_test_info(test):
    if not isinstance(test, unittest.TestCase):
        return

    file_path = inspect.getfile(test.__class__)
    class_name = test.__class__.__name__
    test_name = test._testMethodName
    errors = []

    try:
        guid = getattr(test.__class__, test_name).guid
        if not guid:
            errors.append(f'Test method {file_path}:{class_name}.{test_name} must have a guid.')
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
    owner = None
    features = None
    try:
        owner = getattr(test.__class__, test._testMethodName).owner
        features = getattr(test.__class__, test._testMethodName).features
    except AttributeError:
        try:
            owner = test.__class__.owner
            features = test.__class__.features
        except AttributeError:
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
        'logFile': None,
        'runDate': datetime.today().isoformat()
    }


def get_tests_from_suites(suites) -> List[unittest.TestCase]:
    for suite in suites:
        for tests in suite:  # type: unittest.TestSuite
            if len(tests._tests) > 0:
                setUpClass, tearDownClass = tests._tests[0].setUpClass, tests._tests[0].tearDownClass
                setUpClass()
                for test in tests:
                    yield test
                tearDownClass()


if __name__ == '__main__':
    temp = NamedTemporaryFile(dir=os.path.dirname(__file__), mode='w', suffix='.json')
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
    # print(start_dir)
    suites = loader.discover(start_dir)
    current_suite = None
    new_suite = False
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
        logger.log_to_html()

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

        temp.write(json.dumps(metadata) + "\n")
        temp.flush()
        # print(json.dumps(metadata, indent=4))

        # Run this for each test we make
        # We will change to the directory that has the logs in it
        os.chdir(new_log_dir)
        # then we get the file name that we created
        html_file = Path(new_logfile)
        file_to_push = html_file.name
        # We will push this file
        FTPServer.send_file(test_html=file_to_push)

    json_output = []
    with open(temp.name, 'r') as f:
        for line in f.readlines():
            json_output.append(dict(json.loads(line)))

    spin = SPIN()

    for test in json_output:
        metadata = TestMetaData(test)
        # Get the current test info.
        current_test_info = spin.query(spin.TestInfo.fetch(metadata.guid))
        if not current_test_info:
            new_test_info = spin.query(spin.TestInfo.insert(
                test_guid=metadata.guid,
                test_name=metadata.test_name,
                file_path=metadata.file_path,
                created=metadata.last_run,
                last_run=metadata.last_run
            ))
            current_test_info = spin.query(spin.TestInfo.fetch(metadata.guid))

        # we have test id that matched now we just need check last run and consecutive failures
        # get the last result
        if metadata.result == "failed":
            latest_result = spin.query(spin.TestResults.fetch_most_recent(current_test_info[spin.TestInfo.testId]))
            new_fails = latest_result[spin.TestResults.consecutiveFailures] + 1
        else:
            new_fails = 0

        # Set the correct value for the results, the db expects and int
        if metadata.result == "passed":
            metadata.result = 1
        elif metadata.result == "failed":
            metadata.result = 2
        elif metadata.result == "skipped":
            metadata.result = 3
        else:
            print(f'Got unexpected test status: {metadata.result}')

        # Set the correct log_file, we need it to match what is on the database
        today = datetime.now()
        metadata.log_file = str(today.year) + '/' + str(today.month) + '/' + str(today.day) + '/' + html_file.name

        updated_info = spin.query(spin.TestResults.insert(
            test_id=current_test_info['TestInfo.testId'][0],
            test_result=metadata.result,
            log_file=metadata.log_file,
            consecutive_fails=new_fails,
            run_date=metadata.run_date,
            time_lapse=metadata.lapse
        ))

    temp.close()

# TODO: Need to populate the TestAnnotations, TestAnnotationLabels, TestAnnotationValues and TestResultValues

