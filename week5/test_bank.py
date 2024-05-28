from bank import value


# return 100 when no hello or h


def test_any():
    assert value("sup") == 100

# return 20 when starts with h


def test_h():
    assert value("hi") == 20
    assert value("Hi") == 20

# return 0 when starts with hello


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0