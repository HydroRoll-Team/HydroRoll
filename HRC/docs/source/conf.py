# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib

DATA = None
PYPROJECT = os.path.join("..", "..", "Cargo.toml")
with open(PYPROJECT, "r", encoding="utf8") as f:
    pyproject = f.read()
    DATA = tomllib.loads(pyproject)
PROJECT_VERSION = DATA["package"]["version"]
PROJECT_NAME = DATA["package"]["name"]
AUTHOR_TABLE = DATA["package"]["authors"]
AUTHORS = ",".join([f"{aut}" for aut in AUTHOR_TABLE])

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = PROJECT_NAME  # "HydroRollCore"
release = PROJECT_VERSION  # "latest"
copyright = "2023-PRESENT, HydroRoll-Team."
author = AUTHORS  # "Hsiang Nianian"

html_title = "HydroRollCore"

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
    "issue": ("https://github.com/HydroRoll-Team/HydroRollCore/%s", "issue %s"),
    "doc": ("https://core.hydroroll.team/zh-cn/latest/%s", "pages/%s"),
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
_html_logo = "https://cdn.jsdelivr.net/gh/HydroRoll-Team/HydroRollCore@main/docs/_static/logo.png"
html_favicon = _html_logo

html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
]

html_theme_options = {
    "announcement": "🎉 <em><a href='#'>documentation</a> is still under construction now, welcome any <a href='contributing.html'>contribution</a>!</em>",
    "source_repository": "https://github.com/HydroRoll-Team/HydroRollCore/",
    "source_branch": "main",
    "source_directory": "docs/source/",
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/HydroRoll-Team/HydroRollCore/",
            "html": "",
            "class": "fa-brands fa-github",
        },
        {
            "name": "Pypi",
            "url": "https://pypi.org/project/hydroroll-core/",
            "html": "",
            "class": "fa-brands fa-python",
        },
    ],
}
