from typing import Protocol

from .item import Item
from .item_enum import ItemName


class UpdateItem(Protocol):
    def update_sell_in(self, item: Item):
        ...

    def update_quantity(self, item: Item):
        ...


class UpdateNormalItem:
    def update_sell_in(self, item: Item):
        item.sell_in = item.sell_in - 1

    def _decrease_item(self, item: Item, decrease_by: int = 1) -> None:
        item.quality = max(0, item.quality - decrease_by)

    def _increase_item(self, item: Item, increase_by: int = 1, max_quantity: int = 50):
        item.quality = min(max_quantity, item.quality + increase_by)

    def update_quantity(self, item: Item):
        self._decrease_item(item, 2) if item.sell_in < 0 else self._decrease_item(item)


class UpdateBackStagePassesItem(UpdateNormalItem):
    def update_quantity(self, item: Item):
        if 10 > item.sell_in >= 5:
            self._increase_item(item, 2)
        elif 5 >= item.sell_in >= 0:
            self._increase_item(item, 3)
        elif item.sell_in < 0:
            item.quality = 0
        else:
            self._increase_item(item)


class UpdateSulFurasItem(UpdateNormalItem):
    def update_sell_in(self, item: Item):
        pass

    def update_quantity(self, item: Item):
        pass


class UpdateAgedBrieItem(UpdateNormalItem):
    def update_quantity(self, item: Item):
        self._increase_item(item, 2) if item.sell_in < 0 else self._increase_item(item)


class UpdateConjuredItem(UpdateNormalItem):
    def update_quantity(self, item: Item):
        self._decrease_item(item, 4) if item.sell_in < 0 else self._decrease_item(
            item, 2
        )


update_item_options: dict = {
    ItemName.AGED_BRIE: UpdateAgedBrieItem,
    ItemName.BACKSTAGE_PASSES: UpdateBackStagePassesItem,
    ItemName.SULFURAS: UpdateSulFurasItem,
    ItemName.CONJURED: UpdateConjuredItem,
}


class UpdateItemFactory:
    @staticmethod
    def create(item_name: str):
        if item_name in update_item_options:
            return update_item_options.get(item_name)()
        return UpdateNormalItem()
