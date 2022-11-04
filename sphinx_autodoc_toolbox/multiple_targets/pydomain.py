from typing import List, Optional, Tuple

from docutils.nodes import Element
from sphinx.addnodes import pending_xref
from sphinx.builders import Builder
from sphinx.domains.python import PythonDomain as SphinxPythonDomain
from sphinx.environment import BuildEnvironment


class PythonDomain(SphinxPythonDomain):
    separator = "|"

    def resolve_xref(
        self,
        env: BuildEnvironment,
        fromdocname: str,
        builder: Builder,
        type: str,
        target: str,
        node: pending_xref,
        contnode: Element,
    ) -> Optional[Element]:
        targets = target.split(self.separator)
        for index, target in enumerate(targets):
            element = super().resolve_xref(env, fromdocname, builder, type, target, node, contnode)
            if element:
                return element

    def resolve_any_xref(
        self,
        env: BuildEnvironment,
        fromdocname: str,
        builder: Builder,
        target: str,
        node: pending_xref,
        contnode: Element,
    ) -> List[Tuple[str, Element]]:
        targets = target.split(self.separator)
        for index, target in enumerate(targets):
            results = super().resolve_any_xref(env, fromdocname, builder, target, node, contnode)
            if results:
                return results
