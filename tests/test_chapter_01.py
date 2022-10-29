import pytest
from impractical_python.Chapter_01.pseudonyms_main_fixed import gen_pseudonyms
from impractical_python.Chapter_01.pig_latin_practice import piglatinize
from impractical_python.Chapter_01.etaoin import etaoin


def test_gen_pseudonyms():
    gen = gen_pseudonyms()
    for _ in range(20):
        assert 2 <= len(next(gen).split()) <= 4


@pytest.mark.parametrize("test_input,expected", [
    ("rotten", "ottenray"),
    ("nix", "ixnay"),
    ("ugly", "uglyway"),
    ("o", "oway"),
    ("test", "esttay")
])
def test_piglatin(test_input, expected):
    assert piglatinize(test_input) == expected


@pytest.mark.skip(reason="test not implemented")
def test_etaoin():
    from collections import defaultdict
    assert isinstance(etaoin("Sample text"), defaultdict)
