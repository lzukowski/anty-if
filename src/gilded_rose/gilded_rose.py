from typing import List

from .item import Item


class GildedRose:
    def __init__(self, items: List[Item]) -> None:
        self.items = items

    def update_quality(self) -> None:
        raise NotImplementedError
