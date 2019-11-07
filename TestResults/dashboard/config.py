import os


DEBUG = True if os.environ.get('VT_DEBUG', '0') == '1' else False
HOST = '127.0.0.1' if DEBUG else '0.0.0.0'
PORT = 8080 if DEBUG else 80
HOSTNAME = 'http://%s:%s' % (HOST, PORT) if DEBUG else 'http://testresults.venqa.venafi.com'
API_URL = HOSTNAME + '/api'
