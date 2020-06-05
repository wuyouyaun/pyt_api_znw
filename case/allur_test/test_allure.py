import requests
from case.allur_test.common_function import login,add_buylist

# os.environ['host']="http://open.ap88.com:8900"
def test_01():
    '''用例1描述：xxx'''
    print("测试用例1")

def test_02():
    '''用例1描述：xxx'''
    print("测试用例2")


def test_add_buylist(login_fixture):
    s=login_fixture
    add_buy=add_buylist(s)
    assert add_buy['errorCode']=="01000004"


















