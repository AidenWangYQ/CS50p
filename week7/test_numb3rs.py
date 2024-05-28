from numb3rs import validate


# check for proper regular expression
def test_regex():
    assert validate("127.0.0.1") == True
    assert validate("0.256.256.256") == False
    assert validate("127.0.1") == False
    assert validate("127.0.0.0.1") == False
    assert validate("cat") == False
    