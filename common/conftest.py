# import pytest
# import requests
# from common.common_client import login
# import os
# from case.business_type.read_yaml import yamldata
#
# @pytest.fixture(scope="session")
#
# def unlogin_fixture():
#     print("不登录")
#     s=requests.session()
#     return s
#
#
#
# @pytest.fixture(scope="session")
#
# def login_fixture():
#     s=requests.session()
#     login(s)
#     if not s.headers.get('Authorization',""):
#         pytest.skip("跳过后面的用例")
#     yield s
#     s.close()