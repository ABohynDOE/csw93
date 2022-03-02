# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath("../../csw93"))


# -- Project information -----------------------------------------------------

project = "csw93"
copyright = "2022, Alexandre Bohyn"
author = "Alexandre Bohyn"

# The full version, including alpha/beta/rc tags
release = "0.1.0"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", 'sphinxcontrib.bibtex']

# Add the path to the bibliography file that will be used by the sphinxcontrib.bibtex
# extension.
# The file should be a BibTex file in .bib format
bibtex_bibfiles = ["references.bib"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# Choose the bibliography style among four choices: alpha, unsrt, plain, unsrtalpha.
# The default is alpha
bibtex_default_style = 'unsrt'

# Define the referencing style of the bibliography entries. Available styles are:
# label, author_year, super. The default is label
bibtex_reference_style = "author_year"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
