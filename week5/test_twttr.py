# tests 'shorten' function in twtter.py

from twttr import shorten

# check lowercase vowels removed
def test_lower():
    assert shorten("saeiou") == "s"


# check uppercase vowels removed
def test_upper():
    assert shorten("sAEIOU") == "s"

# check non-vowels are not removed
def test_non_vowel():
    assert shorten("1234567890") == "1234567890"
    assert shorten("`~!@#$%^&*()-_=+[]\\{|};':,./<>?\"") == "`~!@#$%^&*()-_=+[]\\{|};':,./<>?\""
    assert shorten("bcdfghjklmnpqrstvwxyz") == "bcdfghjklmnpqrstvwxyz"
    assert shorten("BCDFGHJKLMNPQRSTVWXYZ") == "BCDFGHJKLMNPQRSTVWXYZ"


# learning points: test program and test functions must start with 'test_' to use pytest