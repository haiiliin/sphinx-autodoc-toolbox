from typing import List, Tuple, Dict, Any

import sphinx
from sphinx.application import Sphinx
from sphinx.ext.autosummary import Autosummary as SphinxAutosummary, process_generate_options


class Autosummary(SphinxAutosummary):
    separator = "|"
    separator_label = ":"

    def get_items(self, names: List[str]) -> List[Tuple[str, str, str, str]]:
        items = []
        for name in names:
            label = None
            if self.separator_label in name:
                name, label = name.split(self.separator_label, 1)
            items_for_name = super().get_items(name.split(self.separator))
            display_name, sig, summary, real_name = items_for_name[0]
            if len(items_for_name) == 1:
                items.append((label or display_name, sig, summary, real_name))
            else:
                real_names = [item[3] for item in items_for_name]
                real_name = self.separator.join(real_names)
                items.append((label or name, sig, summary, real_name))
        return items


def setup(app: Sphinx) -> Dict[str, Any]:
    app.setup_extension('sphinx.ext.autodoc')
    app.add_directive('autosummary', Autosummary)
    app.connect('builder-inited', process_generate_options)

    return {'version': sphinx.__display_version__, 'parallel_read_safe': True}
