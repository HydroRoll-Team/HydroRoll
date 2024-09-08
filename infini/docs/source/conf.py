# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import infini
import os, sys

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib

DATA = None
PYPROJECT = os.path.join("..", "..", "pyproject.toml")
with open(PYPROJECT, "r", encoding="utf8") as f:
    pyproject = f.read()
    DATA = tomllib.loads(pyproject)
PROJECT_VERSION = DATA["project"]["version"]
PROJECT_NAME = DATA["project"]["name"]
AUTHOR_TABLE = DATA["project"]["authors"]
AUTHORS = ",".join([f"{aut['name']}" for aut in AUTHOR_TABLE])

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = PROJECT_NAME
release = PROJECT_VERSION
copyright = (
    "2023-PRESENT, HydroRoll-Team & Noctisynth, org."
)
author = AUTHORS

html_title = "Infini II"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx.ext.extlinks",
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
extlinks = {
    "issue": ("https://github.com/HydroRoll-Team/infini/%s", "issue %s"),
    "doc": ("https://infini.hydroroll.team/zh-cn/latest/%s", "pages/%s"),
}
source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

locale_dirs = ["../locales/"]  # path is example but recommended.
gettext_compact = False  # optional.
gettext_uuid = True  # optional.

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["../_static"]
_html_logo = (
    "https://cdn.jsdelivr.net/gh/HydroRoll-Team/infini@master/docs/_static/logo.png"
)
html_favicon = _html_logo

html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
]

html_theme_options = {
    "source_repository": "https://github.com/HydroRoll-Team/infini/",
    "source_branch": "master",
    "source_directory": "docs/source/",
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/HydroRoll-Team/infini/",
            "html": "",
            "class": "fa-brands fa-github",
        },
        {
            "name": "Pypi",
            "url": "https://pypi.org/project/infini/",
            "html": "",
            "class": "fa-brands fa-python",
        },
    ],
}
