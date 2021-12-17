import os
import sys
sys.path += [os.path.abspath('..'), os.path.abspath('../..')]
from setup import __version__

# -- Project information -----------------------------------------------------

project = 'PyTPP'
copyright = '2021, Venafi'
author = 'Venafi SPI Team'
version = __version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinxcontrib.napoleon',
    'sphinx.ext.inheritance_diagram'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = "sphinx_rtd_theme"
html_theme_path = ["_themes", ]
html_theme_options = {
    'logo_only': True,
    'display_version': True,
    'prev_next_buttons_location': 'both',
    'style_external_links': False,
    'style_nav_header_background': 'bottom',
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': -1,
    'includehidden': True,
    'titles_only': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = [
    'css/custom.css'
]
html_logo = '_static/images/venafi_logo.png'
html_favicon = '_static/images/favicon.ico'

autoclass_content = 'both'

# region Documentation Variables
string = lambda name, value: f'.. |{name}| replace:: {value}'
link = lambda name, label, href:  f"""
.. |{name}| raw:: html

   <a href="{href}">{label}</a>
"""

variables = [
    string(name='Product', value='PyTPP'),
    link(name='Doc Home Page', label='Venafi TPP WebSDK Documentation', href='https://docs.venafi.com/index.php'),
    link(name='Python Requests library', label='Python Requests library', href='https://docs.python-requests.org/en/latest/')
]

rst_prolog = '\n'.join(variables) + '\n'
# endregion Documentation Variables
