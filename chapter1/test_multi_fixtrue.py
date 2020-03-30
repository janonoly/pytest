import pytest
'''
** 作者：janono QQ交流群：882873912**
'''

#测试账号数据
test_user = ["admin1", "admin2"]
test_psw = ["11111", "22222"]

@pytest.fixture(scope="module")
def input_user(request):
    user = request.param
    print("登陆账号：%s" % user)
    return user

@pytest.fixture(scope="module")
def input_psw(request):
    psw = request.param
    print("登陆密码：%s" % psw)
    return psw

@pytest.mark.parametrize("input_user", test_user, indirect=True)
@pytest.mark.parametrize("input_psw", test_psw, indirect=True)
def test_login(input_user, input_psw):
    a = input_user
    b = input_psw
    print("测试数据%s, %s" % (a,b))
    assert b

