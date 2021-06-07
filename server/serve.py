import flask
import os
import glob
from pathlib import Path
from packaging import version as Version

PACKAGES_PATH = os.path.abspath(r'C:\SPI\spi\packages')
DOCS_PATH = os.path.abspath(r'C:\SPI\spi\docs')
app = flask.Flask(__name__, static_folder=DOCS_PATH)


@app.route('/spi')
@app.route('/spi/docs')
def default_to_versions():
    print(f'redirecting to /spi/docs')
    return flask.redirect(f'/spi/docs/index.html', code=302)


@app.route('/spi/docs/<path:path>')
def docs(path='index.html'):
    path = Path(f'{DOCS_PATH}\\html\\{path}')
    return flask.send_from_directory(
        directory=path.parent,
        filename=path.name
    )


@app.route('/spi/api/latestVersion', methods=['GET'])
def get_latest_version():
    get_version_from_filename = lambda x: os.path.basename(x.replace('pytpp-dev-', '').replace('.tar.gz', ''))
    all_versions = [Version.parse(get_version_from_filename(x)) for x in glob.glob(f'{PACKAGES_PATH}/pytpp-dev*')]
    if not all_versions:
        return flask.abort(400, 'No packages available.')

    latest_version = sorted(all_versions)[-1]
    return flask.jsonify({'latestVersion': str(latest_version)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True, use_reloader=True)

