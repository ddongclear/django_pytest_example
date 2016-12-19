# content of test_sysexit.py
import pytest

#@pytest.mark.parametrize('x','y',[
#    (42,1),(21,2),(7,6)
#    ])

#@pytest.fixture('x','y',[(41,1)])
#def test_answers(x,y):
#    assert x * y == 42

def helloworld(request):
    assert "Hello" == "World"


