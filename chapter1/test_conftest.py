#命令行参数
import pytest
'''
** 作者：janono QQ交流群：882873912**
'''

def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1",
        help="my option: type1 or type2"
    )

@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")

def test_answer(cmdopt):
    if cmdopt == "type1":
        print("first")
    elif cmdopt == "type2":
        print("second")
    assert 1 # to see what was printed
