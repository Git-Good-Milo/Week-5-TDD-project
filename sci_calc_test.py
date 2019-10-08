from sci_calc import *

def test_find_sqrt():
    assert find_sqr(100) == 10.0
    assert find_sqr(25) == 5

def test_find_ceil():
    assert find_ceil(12.7) == 13
    assert find_ceil(21.3) == 22
