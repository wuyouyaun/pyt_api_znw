import pytest
import requests
from case.multipart.login_xadmin_page import login_xadmin

@pytest.fixture(scope="session")
def login_fixture():
    '''
    登录前置操作
    :return:s
    '''
    s=requests.session()
    login_xadmin(s)
    yield s
    s.close()

