# content of test_sysexit.py
import pytest

def test_mytest():
    assert "Helo" =="Helo"

@pytest.mark.parametrize('test,expected',[
    (False,False),
    (False,False),
    (True,False),
    (False,True),
    (False,False),
    (False,False),
])
def test_was_hello(test,expected):
    assert test == expected

