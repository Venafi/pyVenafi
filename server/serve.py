import flask
import os
import glob
from pathlib import Path

PACKAGES_PATH = os.path.abspath(r'C:\SPI\spi\packages')
DOCS_PATH = os.path.abspath(r'C:\SPI\spi\docs')
LATEST_DOC_VERSION = sorted(os.listdir(DOCS_PATH))[-1]
app = flask.Flask(__name__, static_folder=DOCS_PATH)


@app.route('/spi')
@app.route('/spi/docs')
def default_to_versions():
    print(f'redirecting to /spi/docs/{LATEST_DOC_VERSION}')
    return flask.redirect(f'/spi/docs/{LATEST_DOC_VERSION}')


@app.route('/spi/api/latestVersion', methods=['GET'])
def get_latest_version():
    base_version = flask.request.args.get('baseVersion')
    components = []
    if not base_version or not len(components := base_version.split('.')) == 4:
        avail_versions = glob.glob(
            f'{PACKAGES_PATH}/*'
        )
        if not avail_versions:
            return flask.abort(400, 'No packages available.')
    else:
        adjusted_comps = ".".join(components[:-1])
        avail_versions = glob.glob(
            f'{PACKAGES_PATH}/venafi-{adjusted_comps}*'
        )
        if not avail_versions:
            return flask.abort(400, f'No packages available for {adjusted_comps}*.')
    latest = sorted(avail_versions)[-1]
    return os.path.basename(latest.replace('venafi-', '').replace('.tar.gz', ''))


@app.route('/spi/docs/<version>')
def default_to_version_index(version=LATEST_DOC_VERSION):
    print(f'redirecting to /spi/docs/{version}/versions.html')
    return flask.redirect(f'/spi/docs/{version}/versions.html')


@app.route('/spi/docs/<version>/<path:path>')
def docs(version=LATEST_DOC_VERSION, path='index.html'):
    path = Path(f'{DOCS_PATH}\\{version}\\html\\{path}')
    print(path)
    return flask.send_from_directory(
        directory=path.parent,
        filename=path.name
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True, use_reloader=True)
