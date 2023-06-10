import pytest
from mymodule import add

def test_add():
    assert add(2, 2) == 4
    assert add(5, 10) == 15
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-10, 10) == 0
