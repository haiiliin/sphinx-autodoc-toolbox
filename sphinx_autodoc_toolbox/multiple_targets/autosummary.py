from typing import List, Tuple

from sphinx.ext.autosummary import Autosummary as SphinxAutosummary


class Autosummary(SphinxAutosummary):
    separator = "|"
    separator_label = ":"

    def get_items(self, names: List[str]) -> List[Tuple[str, str, str, str]]:
        items = []
        for name in names:
            label = None
            if self.separator_label in name:
                name, label = name.split(self.separator_label, 1)
            items.append(self.get_summary_item(super().get_items(name.split(self.separator)), label))
        return items

    def get_summary_item(self, items: List[Tuple[str, str, str, str]], label: str) -> Tuple[str, str, str, str]:
        real_name = self.separator.join([item[3] for item in items])
        display_name = self.separator.join([item[0] for item in items])
        return label or display_name, items[0][1], items[0][2], real_name
