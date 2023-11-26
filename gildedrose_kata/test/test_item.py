import pytest

from ..src.item import Item
from ..src.gilded_rose import GildedRose

AGED_BRIE = "Aged Brie"
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
CONJURED = "Conjured"


class TestNormalItem:
    def test_item(self):
        items = [Item("foo", 3, 2)]

        assert "foo" == items[0].name
        assert 3 == items[0].sell_in
        assert 2 == items[0].quality

    def test_item_lower_after_each_day(self):
        items = [Item("foo", 2, 3)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert items[0].quality == 2
        assert items[0].sell_in == 1

    def test_item_does_not_change_name_after_update_quality(self):
        items = [Item("foo", 2, 3)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert "foo" == items[0].name

    def test_quality_is_not_negative(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert items[0].quality == 0

    def test_quality_decrease_twice_as_fast_after_sell_in_date(self):
        items = [Item("foo", 0, 5)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        assert items[0].quality == 3


class TestAgedBrieItem:
    def test_quality_maximum_is_50(self):
        items = [Item(AGED_BRIE, 0, 50)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert items[0].quality == 50

    @pytest.mark.parametrize(
        "sell_in, quality, expected_quality", [(1, 2, 3), (0, 4, 6)]
    )
    def test_increase_quality(self, sell_in, quality, expected_quality):
        items = [Item(AGED_BRIE, sell_in, quality)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert items[0].quality == expected_quality


class TestSulfurasItem:
    @pytest.mark.parametrize(
        "sell_in, quality, expected_quality, expected_sell_in",
        [(10, 2, 2, 10), (0, 10, 10, 0), (-1, 5, 5, -1)],
    )
    def test_item_never_decrease_quality(
        self, sell_in, quality, expected_quality, expected_sell_in
    ):
        items = [Item(SULFURAS, sell_in, quality)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        assert expected_quality == items[0].quality
        assert expected_sell_in == items[0].sell_in


class TestBackStagePass:
    @pytest.mark.parametrize(
        "sell_in, quality, expected_quality", [(10, 2, 4), (6, 10, 12), (9, 5, 7)]
    )
    def test_increase_quality_by_2_if_sell_in_less_than_or_equal_10(
        self, sell_in, quality, expected_quality
    ):
        items = [Item(BACKSTAGE_PASSES, sell_in, quality)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        assert expected_quality == items[0].quality

    @pytest.mark.parametrize(
        "sell_in, quality, expected_quality", [(5, 3, 6), (1, 2, 5), (3, 20, 23)]
    )
    def test_increase_quality_by_3_if_sell_in_less_than_or_equal_5(
        self, sell_in, quality, expected_quality
    ):
        items = [Item(BACKSTAGE_PASSES, sell_in, quality)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        assert expected_quality == items[0].quality

    def test_quality_is_0_if_sell_in_is_0(self):
        items = [Item(BACKSTAGE_PASSES, 0, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        assert 0 == items[0].quality

    def test_quality_increase_when_sell_in_greater_than_10(self):
        items = [Item(BACKSTAGE_PASSES, 11, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        assert 11 == items[0].quality


class TestConjuredItem:
    def test_item_decrease(self):
        items = [Item(CONJURED, 3, 5)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        assert 3 == items[0].quality
        assert 2 == items[0].sell_in

    def test_item_decrease_when_sell_in_is_passed(self):
        items = [Item(CONJURED, 0, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        assert -1 == items[0].sell_in
        assert 6 == items[0].quality
