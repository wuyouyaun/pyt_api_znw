import pytest
import requests
import os
from case.allur_test.common_function import login


@pytest.fixture(scope="session")
def login_fixture():
    print("前置操作：登录")
    s=requests.session()
    login(s)
    yield s
    s.close()
#命令行参数，parser是pytest中的内置fixture
def pytest_addoption(parser):
    parser.addoption(
        "--cmdhost",action="store",
        default="http://open.ap88.com:8900",
        help="my option: host1 or host2"
        )
@pytest.fixture(scope="session",autouse=True)
def host(request):
    #获取环境变量，自动生效
    print("获取命令行参数：%s"%request.config.getoption("--cmdhost"))
    os.environ['host']=request.config.getoption("--cmdhost")


