from typing import List

from .inventory import GoodCategory
from .item import Item


class GildedRose:
    def __init__(self, items: List[Item]) -> None:
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            if self._sulfuras(item):
                continue
            good = GoodCategory().build_for(item)
            good.update()
            item.quality = good.quality
            item.sell_in = good.sell_in

    @staticmethod
    def _sulfuras(item: Item) -> bool:
        return item.name == "Sulfuras, Hand of Ragnaros"
