# coding:utf-8
import pytest
'''
** 作者：janono QQ交流群：882873912**
'''
def test_s1(login):
    print("用例1：登陆后其它动作111")

def test_s2():
    print("用例2：不需要登陆222")

def test_s3(login):
    print("用例3：登陆后动作333")