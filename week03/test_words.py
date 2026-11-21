
from words import prefix, suffix
import pytest

def test_prefix():
    assert prefix("cat", "caterpillar") == "cat"
    assert prefix("", "caterpillar") == ""
    assert prefix("cat", "") == ""
    assert prefix("", "") == ""
    assert prefix("correct", "clear") == "c"
    assert prefix("angelic", "awesome") == "a"
    assert prefix("found", "profound") == ""
    assert prefix("ditch", "itch") == ""
    assert prefix("happy", "funny") == ""

def test_suffix():
    assert suffix("", "") == ""
    assert suffix("", "correct") == ""
    assert suffix("clear", "") == ""
    assert suffix("angelic", "awesome") == ""
    assert suffix("found", "profound") == "found"
    assert suffix("ditch", "itch") == "itch"
    assert suffix("happy", "funny") == "y"
    assert suffix("tired", "fatigued") == "ed"
    assert suffix("swimming", "FLYING") == "ing"

pytest.main(["-v", "--tb=line", "-rN", __file__])
