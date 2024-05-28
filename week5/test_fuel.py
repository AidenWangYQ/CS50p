import pytest
from fuel import convert, gauge

# checks validity of responses from convert
def test_convert():
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    assert convert("1/2") == 50


# checks validity of responses from gauge
def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"