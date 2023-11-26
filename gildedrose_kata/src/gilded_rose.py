from .item import Item
from .updated_item_protocol import UpdateItemFactory


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self._upgrade_single_item_quality(item)

    def _upgrade_single_item_quality(self, item: Item):
        update_item = UpdateItemFactory.create(item.name)
        update_item.update_sell_in(item)
        update_item.update_quantity(item)
