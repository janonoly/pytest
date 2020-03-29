import pytest
'''
** 作者：janono QQ交流群：882873912**
'''

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

def f():
    raise  SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()
