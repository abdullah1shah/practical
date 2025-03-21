import pytest

from main import subtract

def test_subtract():
    assert subtract(2,3)==-1
    assert subtract(4,6)==-2
    assert subtract(-1,-1)==2