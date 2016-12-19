# content of test_sysexit.py
import pytest
from datetime import time

@pytest.mark.parametrize('test,expected',[
    (False,False),
    (True,False),
    (False,True),
    (False,False),
])
def tests_im_hello(test,expected):
    assert test == expected


@pytest.mark.parametrize('time_of_day',[
    time(10)
   ])
def tests_was_hello(time_of_day):
    if time(5) < time_of_day < time(12):
        return "morning"
    elif time(18) < time_of_day < time(21):
        return "evening"


@pytest.fixture(scope='function')
def x(request):
        return request.param * 3

@pytest.fixture(scope='function')
def y(request):
        return request.param * 2


@pytest.mark.parametrize('x, y', [('a', 'b')], indirect=['x'])
def test_indirect(x,y):
    assert x == 'aaa'
    assert y == 'b'
