# Configuration file for the Sphinx documentation builder.
#
# This file only contains a few common options.
# For the full list, see: https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------
# Nothing needed, as long as `sphinxcontrib.csharpdomain` is importable.
# If it isn't importable, then you'll need to manually point Python at the
# namespace package. From what I can see, this isn't cleanly supported, so you'd
# need to uncomment the following (hacky) lines or find another solution:
#
#     import importlib, pathlib
#
#     import sphinxcontrib
#     sphinxcontrib = importlib.reload(sphinxcontrib)
#     sphinxcontrib.__path__.append(str(pathlib.Path('.').resolve().parent / 'sphinxcontrib'))
#
# Hopefully, I can rewrite this snippet to use sys.path instead of the namespace
# package's own `__path__` attribute, but no reasonable attempt has worked.


# -- Project information -----------------------------------------------------

project = 'sphinxcontrib-csharpdomain'
copyright = '2020, Sam Redmond'
author = 'Sam Redmond'

# The full version, including alpha/beta/rc tags.
release = '0.0.1'


# -- General configuration ---------------------------------------------------
# See: https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# For this documentation, we'll only need to use the csharpdomain subpackage.
# See: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-extensions
extensions = [
    'sphinxcontrib.csharpdomain'
]

# Ignored file patterns when looking for source files.
# See: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-exclude_patterns
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# When in nitpicky mode, tell Sphinx to ignore a few specific missing targets.
# See: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-nitpick_ignore
nitpick_ignore = [
    ('csharp:type', 'void'),
    ('csharp:type', 'T'),
]


# -- Options for HTML output -------------------------------------------------
# See: https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The "theme" for HTML output.
# See: https://www.sphinx-doc.org/en/master/usage/theming.html
html_theme = 'pyramid'
