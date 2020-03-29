import pytest
'''
** 作者：janono QQ交流群：882873912**
'''

def f():
    return 3

def test_function():
    assert f() == 4

def test_zero_division():
    #excinfo 是一个异常信息实例，异常的包装器。主要属性有type，value,traceback
    with pytest.raises(ZeroDivisionError) as excinfo:
        1 / 0
    # 断言异常类型type
    assert excinfo.type == ZeroDivisionError
    # 断言异常value值
    assert "division by zero" in str(excinfo.value)

#常用断言：
#assert xx判断xx为真
#assert not xx 判断xx不为真
#assert a in b 
#assert a == b
#assert a ！= b

