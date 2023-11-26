import pytest

from parrot_kata.src.parrot import Parrot, ParrotType, ParrotFactory


def test_speedOfEuropeanParrot():
    parrot = ParrotFactory.create(ParrotType.EUROPEAN, 0, 0, False)
    assert parrot.speed() == 12.0


def test_cryOfEuropeanParrot():
    parrot = ParrotFactory.create(ParrotType.EUROPEAN, 0, 0, False)
    assert parrot.cry() == "Sqoork!"


def test_speedOfAfricanParrot_With_One_Coconut():
    parrot = ParrotFactory.create(ParrotType.AFRICAN, 1, 0, False)
    assert parrot.speed() == 3.0


def test_cryOfAfricanParrot():
    parrot = ParrotFactory.create(ParrotType.AFRICAN, 1, 0, False)
    assert parrot.cry() == "Sqaark!"


def test_speedOfAfricanParrot_With_Two_Coconuts():
    parrot = ParrotFactory.create(ParrotType.AFRICAN, 2, 0, False)
    assert parrot.speed() == 0.0


def test_speedOfAfricanParrot_With_No_Coconuts():
    parrot = ParrotFactory.create(ParrotType.AFRICAN, 0, 0, False)
    assert parrot.speed() == 12.0


def test_speedNorwegianBlueParrot_nailed():
    parrot = ParrotFactory.create(ParrotType.NORWEGIAN_BLUE, 0, 1.5, True)
    assert parrot.speed() == 0.0


def test_speedNorwegianBlueParrot_not_nailed():
    parrot = ParrotFactory.create(ParrotType.NORWEGIAN_BLUE, 0, 1.5, False)
    assert parrot.speed() == 18.0


def test_speedNorwegianBlueParrot_not_nailed_high_voltage():
    parrot = ParrotFactory.create(ParrotType.NORWEGIAN_BLUE, 0, 4, False)
    assert parrot.speed() == 24.0


def test_cryNorwegianBlueParrot_high_voltage():
    parrot = ParrotFactory.create(ParrotType.NORWEGIAN_BLUE, 0, 4, False)
    assert parrot.cry() == "Bzzzzzz"


def test_cryNorwegianBlueParrot_no_voltage():
    parrot = ParrotFactory.create(ParrotType.NORWEGIAN_BLUE, 0, 0, False)
    assert parrot.cry() == "..."


def test_invalid_parrot_type():
    with pytest.raises(KeyError) as exc_info:
        parrot = ParrotFactory.create("something weird", 1, 2, False)

    assert "Invalid parrot type" in str(exc_info.value)
