# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import datetime
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme

# -- Project information -----------------------------------------------------
project = 'finf'
copyright = f'{datetime.date.today().year}, finf, kwok3626@gmail.me'
#copyright =f '2023blgxwk, gudut@outlook.com, gn, Last updated on {datetime.date.today().year}'
author = 'Kwok'
version = 'v0.1'
release = version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
# The master toctree document.
master_doc = 'index'
# pip insatll recommonmark
# pip install sphinx_markdown_tables
extensions = [
    'recommonmark', 
    'sphinx_markdown_tables',
    'sphinxcontrib.mermaid', 
    'sphinx_copybutton',
    # 'myst_parser'
    'sphinx.ext.githubpages',
    'sphinx_rtd_size' # need 'pip install sphinx-rtd-size'
    ]

sphinx_rtd_size_width = "100%"  # change the width of the content block of the "Read the Docs" theme

source_suffix = {'.rst': 'restructuredtext','.md': 'markdown', '.txt': 'markdown'}

templates_path = ['_tesmplates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
default_role = "obj"

myst_enable_extensions = [
    "tasklist",
    "deflist",
    "dollarmath",
    ]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'analytics_anonymize_ip': False,
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 3,
    'includehidden': True,
    'titles_only': False,
    'style_nav_header_background': '#3d3f47',
    # 'github_url': 'https://github.com/ngaodut/scibro'
    # Remove the line that sets body_max_width to Auto
    }

# html_theme_options = {
#     'body_max_width': None
#     }

html_context = {
    'display_github': True,
    'github_user': 'guoyangzhe',
    'github_repo': 'finf',
    'github_version': 'master',
    }

html_title = 'finf'

html_favicon = 'favicon.png' # 或者 'favicon.ico'
html_logo = "../media/rest-syntax/pic-video/logo-1.png"
html_static_path = ['_static']
html_last_updated_fmt = '%a, %d %b %Y %H:%M:%S'
