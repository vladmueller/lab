# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SimplePDF Test'
copyright = '2025, Vladimir Müller'
author = 'Vladimir Müller'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- SimplePDF Options -------------------------------------------------------

simplepdf_vars = {
    'primary': '#FFFF00',
    'primary-opaque': '#FFFF00',
    'secondary': 'orange',
    'white': '#0000FF',
    'links': '#0000FF',
    'cover-bg': '#FFFF00',
    'cover': '#0000FF',
}

def setup(app):
    app.add_css_file('custom.css')    
