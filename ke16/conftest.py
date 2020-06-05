import pytest
import requests
from ke15.login_xadmin_page import login_xadmin
import os

# 添加命令行参数  parser内置fixture
def pytest_addoption(parser):
    parser.addoption(
        "--cmdhost", action="store",
        default="http://49.235.92.12:8030",
        help="my option: host1 or host2"
    )


@pytest.fixture(scope="session", autouse=True)
def host(request):
    '''设置环境变量，自动生效'''
    os.environ["host"] = request.config.getoption("--cmdhost")





# request 是pytest内置的fixture

@pytest.fixture(scope="session")
def login_fixture(request):
    '''登陆 前置操作'''
    s = requests.session()
    # 先登陆
    login_xadmin(s)

    def close_s():
        s.close()
    def close_x():
        print("关闭其他的")
    request.addfinalizer(close_s)
    request.addfinalizer(close_x)
    return s



    # yield s
    # print("数据清理，后置操作")
    # s.close()