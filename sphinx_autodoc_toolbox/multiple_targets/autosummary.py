import re
from typing import List, Tuple

from sphinx.ext.autosummary import Autosummary as SphinxAutosummary


class Autosummary(SphinxAutosummary):
    separator = "|"
    separator_summary = "->"

    def get_items(self, names: List[str]) -> List[Tuple[str, str, str, str]]:
        items = []
        for name in names:
            summary_name = None
            if self.separator_summary in name:
                summary_name, name = re.split(rf"[{self.separator_summary}\s]+", name, 1)
            items.append(self.get_summary_item(super().get_items(re.split(rf"[{self.separator}\s]+", name)),
                                               summary_name))
        return items

    def get_summary_item(self, items: List[Tuple[str, str, str, str]], summary_name: str) -> Tuple[str, str, str, str]:
        if len(items) == 1:
            return items[0]
        real_name = self.separator.join([item[3] for item in items])
        display_name = self.separator.join([item[0] for item in items])
        for index, (_, _, _, name) in enumerate(items):
            if summary_name and summary_name in name:
                return items[index][0], items[index][1], items[index][2], real_name
        return display_name, items[0][1], items[0][2], real_name
