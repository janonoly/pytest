# coding:utf-8
import pytest
'''
** 作者：janono QQ交流群：882873912**
'''
@pytest.fixture(scope="module")
def open():
    print("打开浏览器")

@pytest.fixture(scope="module")
def open1():
    print("打开浏览器")
    yield
    print("执行teardown")
    print("最后关闭浏览器")


def test_s1(open1):
    print("用例1：")

def test_s2(open1):
    print("用例2")

    #如果第一个用例异常了，不影响其他的用例执行
    #如果在setup就异常了，那么是不会去执行yeild后面的teardown内容
    #yield也可以配合with语句使用，以下是官方文档
    raise NameError

def test_s3(open1):
    print("用例3")
if __name__ == "__main__":
    pytest.main(["-s", "test_f1.py"])