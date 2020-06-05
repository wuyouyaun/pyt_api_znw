import pytest
from common.common_client import login
import requests

# @pytest.fixture(scope="session")
# def login_fixture():
#     s=requests.session()
#     print("\n233测试数据")
#     yield s
#     s.close()

# request 是pytest内置fixture
@pytest.fixture(scope="session")
def login_fixture(request):
    s=requests.session()
    login(s)

    def close():
        s.close()
    request.addfinalizer(close)   # 终结函数，先返回s ,再执行终结函数关闭fixture打开的资源
    return s






