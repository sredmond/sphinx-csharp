"""
    sphinxcontrib.csharpdomain
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    This extension provides a Sphinx domain for documenting C# source files.

    :copyright: Copyright 2020 by Sam Redmond <author_email>
    :license: MIT, see LICENSE for details.
"""
from .csharp import CSharpDomain

__version__ = '0.0.1'

def setup(app):
    app.add_domain(CSharpDomain)
