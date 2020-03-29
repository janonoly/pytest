import pytest
'''
** 作者：janono QQ交流群：882873912**
'''

class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
