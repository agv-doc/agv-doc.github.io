# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'AGV-RestAPI-Doku'
copyright = '2025, Robert Berger'
author = 'Robert Berger'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',          # Google/NumPy-Style Docstrings (falls nötig)
    'sphinx.ext.autosectionlabel',  # erlaubt Querverweise auf Überschriften
    'sphinxcontrib.httpdomain',     # schöne HTTP/API-Direktiven
    # 'myst_parser',                # <-- NUR aktivieren, wenn du Markdown möchtest
]

templates_path = ['_templates']
exclude_patterns = []

rst_epilog = f"""
.. |release| replace:: {release}
.. |author| replace:: {author}
"""

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
