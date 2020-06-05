import requests
import pytest


def test_ces_login(login_fixture):
    s=login_fixture
    print("11111")
    print(s)
    a=1
    b=2
    c=a+b
    assert c==3

# if __name__=="__main__":
#
#     h=ces_login(login_xmain)
#     print(h)
