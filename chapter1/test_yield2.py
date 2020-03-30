#coding:utf-8
#官方文档案例
#content of test_yield2.py

import smtplib
import pytest

'''
** 作者：janono QQ交流群：882873912**
'''

@pytest.fixture(scope="module")
def smtp():
    with smtplib.SMTP("smtp.gmail.com") as smtp:
        yield smtp # provide the fixture value

