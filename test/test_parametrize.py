#coding:utf-8

import pytest
'''
** 作者：janono QQ交流群：882873912**
'''

#pytest.mark.parametrize装饰器可以实现测试参数化
@pytest.mark.parametrize("test_input,expected",
                         [ ("3+5", 8),
                           ("2+4", 6),
                           ("6 * 9", 42),
                           ])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

#参数组合
@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    print("测试数据组合: x->%s, y->%s" % (x, y))

