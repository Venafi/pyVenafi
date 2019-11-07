import keyring
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta
from toolkit.sqlTools import venafiTesting as VT
from toolkit.sqlTools.sqlHelper import SQLCommandBuilder as Ops
import time
from BeautifulSoup import BeautifulSoup as bs
import requests
import json
from dashboard import config
from dateutil.parser import parser


def get_all_view(frameworkName):
    data = {
        'frameworkNames': frameworkName,
        'startDate': (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d'),
        'endDate': (datetime.today()).strftime('%Y-%m-%d'),
        'latestResultOnly': True,
        'failuresOnly': True
    }

    resp = requests.get('http://testresults.venqa.venafi.com/api/viewAll', data=json.dumps(data))
    return resp.json() if resp.status_code == 200 else {}

def send_email(from_addr, from_pass, to_addr, message):
    print('\tSending e-mail...')
    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    server.starttls()
    server.login(from_addr, from_pass)
    server.sendmail(from_addr, to_addr, message)
    server.quit()
    print('\tE-mail sent!')

class VTSQLTables:
    def __init__(self):
        self.RunsTable = VT.Runs()
        self.FrameworksTable = VT.Frameworks()
        self.JobsTable = VT.Jobs()
        self.JobHistoryTable = VT.JobHistory()
        self.TestsTable = VT.Tests()
        self.TestHistoryTable = VT.TestHistory()
        self.VenafiTesting = VT.VenafiTesting()
        self.ops = Ops()

class HTML:
    def __init__(self, obj, text='', styles=''):
        self.starter = "<%s %s>" % (obj, styles)
        self.finisher = "</%s>" % obj
        self.text = text
        self.children = []

    def __str__(self):
        string = self.starter + self.text
        for child in self.children:
            string += child.__str__()
        string += self.finisher
        return string

    def __show__(self):
        pass

    def add_child(self, child):
        self.children.append(child)

    def add_children(self, children):
        for child in children:
            self.add_child(child)


class Table:
    def __init__(self, title):
        table = HTML('table')
        tbody = HTML('tbody')
        tr = HTML('tr')
        td = HTML('td')
        table.add_child(tbody)
        tbody.add_child(tr)
        tr.add_child(td)

        self.table = table
        self.job = td
        self.className = td
        self.testName = td

    def new_job(self, new_job):
        job = HTML(
            obj='li',
        )
        job.add_child(
            HTML(
                obj='strong',
                text=new_job
            )
        )
        job.add_child(
            HTML(
                obj='ul'
            )
        )
        self.job.add_child(job)
        self.className = self.job.children[-1].children[-1]

    def new_class(self, new_class_name):
        new_className = HTML(
            obj='li'
        )

        new_className.add_child(
            HTML(
                obj='em',
                text=new_class_name
            )
        )
        new_className.add_child(
            HTML(
                obj='ul'
            )
        )
        self.className.add_child(new_className)
        self.testName = self.className.children[-1].children[-1]

    def new_test(self, new_test, age, is_new, is_resolved, is_under_construction):
        if int(age) > 0:
            text = "%s =&gt; Age = %s" % (new_test, age)
            if is_resolved:
                color = 'style="color: #0606c6"'
            elif is_under_construction:
                color = 'style="color: #CCCC00"'
            else:
                color = 'style="color: #800000"'
        else:
            text = new_test
            color = 'style="color: #008000"'

        if is_new is True:
            text += "<em> (New)</em>"

        newTest = HTML(
            obj='li',
            text=text,
            styles=color
        )
        newTest.add_child(
            HTML(
                obj='ul'
            )
        )
        self.testName.add_child(newTest)


def create_html_file(framework):

    vt = VTSQLTables()
    vt.FrameworksTable.load_framework(framework.lower())

    desired_columns = [
        vt.JobsTable.Columns.name.aliased_name,
        vt.TestHistoryTable.Columns.testId.aliased_name,
        vt.TestsTable.Columns.className.aliased_name,
        vt.TestsTable.Columns.testName.aliased_name,
        vt.TestHistoryTable.Columns.testResult.aliased_name,
        vt.TestHistoryTable.Columns.resolution.aliased_name,
        vt.TestsTable.Columns.lastUpdated.aliased_name,
        vt.TestHistoryTable.Columns.age.aliased_name
    ]

    all_data = get_all_view(frameworkName=framework)
    if not all_data:
        rows_for_today = {}
    else:
        keys, values = all_data
        rows = zip(*values)
        rows_for_today = {k:v for k, v in dict(zip(keys, rows)).items() if k in desired_columns}

    title = HTML(
        obj='h1',
        text='%s AUTOMATION RESULTS' % framework.upper(),
        styles='style="text-align:center"'
    )
    date = HTML(
        obj='p',
        styles='style="text-align:center"'
    )
    date.add_child(
        HTML(
            obj='strong',
            text='Date: %s' % time.strftime('%d %b, %Y')
        )
    )

    title.add_children([date])

    if not rows_for_today:
        no_failures = HTML(
            obj='p',
            styles='style="text-align:center"'
        )
        no_failures.add_child(
            HTML(
                obj='strong',
                text='NO FAILURES TODAY!!!',
                styles='style="color: green"'
            )
        )
        title.add_children([no_failures])

    else:
        horizontal_bar = HTML(
            obj='hr'
        )

        product_bugs = Table('Product Bugs')
        pb =False
        current_pb_job = ''
        current_pb_class = ''

        under_construction = Table('Under Construction')
        uc = False
        current_uc_job = ''
        current_uc_class = ''

        fixed = Table('Fixed')
        fx = False
        current_fx_job = ''
        current_fx_class = ''

        undetermined = Table('Undetermined')
        ud = False
        current_ud_job = ''
        current_ud_class = ''

        ignored = Table('Ignored')
        ig = False
        current_ig_job = ''
        current_ig_class = ''

        resolved = Table('Resolved')
        rs = False
        current_rs_job = ''
        current_rs_class = ''

        for i, job_name in enumerate(sorted(rows_for_today.get(vt.JobsTable.Columns.name.aliased_name, []))):
            testClass = rows_for_today[vt.TestsTable.Columns.className.aliased_name][i].strip()
            testName = rows_for_today[vt.TestsTable.Columns.testName.aliased_name][i].strip()
            age = rows_for_today[vt.TestHistoryTable.Columns.age.aliased_name][i]
            resolution = rows_for_today[vt.TestHistoryTable.Columns.resolution.aliased_name][i].strip()
            lastUpdated = rows_for_today[vt.TestsTable.Columns.lastUpdated.aliased_name][i]

            yesterday = datetime.today() - timedelta(days=1)
            fmt = lambda x, y: datetime.strftime(parser().parse(x), y)
            is_new = fmt(lastUpdated, '%Y%m%d%H%M%S') >= fmt(str(yesterday), '%Y%m%d000000') and age == 3

            if resolution == 'Product Bug':
                pb = True

                if current_pb_job != job_name:
                    current_pb_job = job_name
                    product_bugs.new_job(job_name)

                if current_pb_class != testClass:
                    current_pb_class = testClass
                    product_bugs.new_class(testClass)

                product_bugs.new_test(testName, age, is_new, False, False)

            elif resolution == 'Under Construction':
                uc = True

                if current_uc_job != job_name:
                    current_uc_job = job_name
                    under_construction.new_job(job_name)

                if current_uc_class != testClass:
                    current_uc_class = testClass
                    under_construction.new_class(testClass)

                under_construction.new_test(testName, age, is_new, False, True),

            elif resolution == 'Fixed':
                fx = True

                if current_fx_job != job_name:
                    current_fx_job = job_name
                    fixed.new_job(job_name)

                if current_fx_class != testClass:
                    current_fx_class = testClass
                    fixed.new_class(testClass)

                fixed.new_test(testName, age, is_new, False, False)

            elif resolution == 'Resolved':
                rs = True

                if current_rs_job != job_name:
                    current_rs_job = job_name
                    resolved.new_job(job_name)

                if current_rs_class != testClass:
                    current_rs_class = testClass
                    resolved.new_class(testClass)

                resolved.new_test(testName, age, is_new, True, False)

            elif resolution == 'Ignored':
                ig = True

                if current_ig_job != job_name:
                    current_ig_job = job_name
                    ignored.new_job(job_name)

                if current_ig_class != testClass:
                    current_ig_class = testClass
                    ignored.new_class(testClass)

                ignored.new_test(testName, age, is_new, False, False)

            elif resolution == 'Undetermined':
                ud = True

                if current_ud_job != job_name:
                    current_ud_job = job_name
                    undetermined.new_job(job_name)

                if current_ud_class != testClass:
                    current_ud_class = testClass
                    undetermined.new_class(testClass)

                undetermined.new_test(testName, age, is_new, False, False)

            else:
                print('ERROR: Resolution is %s, which was not expected.' % resolution)
                continue

        if pb is True:
            pb_title = HTML(
                obj="h3",
                text="Product Bugs",
                styles='style="text-align:center"'
            )
            title.add_children(
                [
                    horizontal_bar,
                    pb_title,
                    product_bugs.table
                ]
            )
        if uc is True:
            uc_title = HTML(
                obj="h3",
                text="Under Construction",
                styles='style="text-align:center"'
            )
            title.add_children(
                [
                    horizontal_bar,
                    uc_title,
                    under_construction.table
                ]
            )
        if rs is True:
            rs_title = HTML(
                obj="h3",
                text="Resolved But Not Merged",
                styles='style="text-align:center"'
            )
            title.add_children(
                [
                    horizontal_bar,
                    rs_title,
                    resolved.table
                ]
            )
        if fx is True:
            fx_title = HTML(
                obj="h3",
                text="Fixed",
                styles='style="text-align:center"'
            )
            title.add_children(
                [
                    horizontal_bar,
                    fx_title,
                    fixed.table
                ]
            )
        if ud is True:
            ud_title = HTML(
                obj="h3",
                text="Undetermined",
                styles='style="text-align:center"'
            )
            title.add_children(
                [
                    horizontal_bar,
                    ud_title,
                    undetermined.table
                ]
            )
        if ig is True:
            ig_title = HTML(
                obj="h3",
                text="Ignored",
                styles='style="text-align:center"'
            )
            title.add_children(
                [
                    horizontal_bar,
                    ig_title,
                    ignored.table
                ]
            )

    email = title

    html = bs(email.__str__())
    pretty_html = html.prettify()
    # print(pretty_html)


    FROM_USER = 'tyler.spens'
    FROM_PASS = keyring.get_password('VEN', FROM_USER)
    FROM = '%s@venafi.com'%FROM_USER
    TO = [
        'ServerCert@venafi.com',
        'tatyana.nikolaeva@venafi.com',
        'jordan.roquet@venafi.com',
        'dave.lindsey@venafi.com'
    ]
    MESSAGE = MIMEText(pretty_html, 'html')

    MESSAGE['Subject'] = '%s Automation Results' % framework.title()
    MESSAGE['FROM'] = FROM
    MESSAGE['TO'] = ', '.join(TO)

    send_email(from_addr=FROM, from_pass=FROM_PASS, to_addr=TO, message=MESSAGE.as_string())


if __name__ == '__main__':
    print('Getting Python Automation Results.....')
    create_html_file('Python')
    print('Getting Integration Automation Results.....')
    create_html_file('Integration')
