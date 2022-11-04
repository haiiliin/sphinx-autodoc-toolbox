from typing import Dict, Any

import sphinx
from sphinx.application import Sphinx
from sphinx.domains.python import filter_meta_fields, builtin_resolver
from sphinx.ext.autosummary import process_generate_options

from .autosummary import Autosummary
from .pydomain import PythonDomain


def setup(app: Sphinx) -> Dict[str, Any]:
    app.setup_extension('sphinx.ext.autodoc')
    app.add_directive('autosummary', Autosummary)
    app.connect('builder-inited', process_generate_options)

    app.setup_extension("sphinx.directives")
    app.add_domain(PythonDomain, override=True)
    app.connect("object-description-transform", filter_meta_fields)
    app.connect("missing-reference", builtin_resolver, priority=900)

    return {
        "version": "0.0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
