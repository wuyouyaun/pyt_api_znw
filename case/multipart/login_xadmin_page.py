import requests
import re
import pytest
# @pytest.fixture(scope="function")
# def delect_teacher():
#     '''新增老师标签前清空测试数据'''
#     sql="delete  from djangoweb.hello_teacher WHERE teacher_name = '11小测试';"
#     execute_sql(sql)
#     yield
#     print("数据清理")
def login_xadmin(s):
    # s=requests.session()
    url ="http://49.235.92.12:8020/xadmin/"
    r1=s.get(url)
    print(r1.text)
    csrfmiddlewaretoken=re.findall(r"value='(.+)' ",r1.text)
    print(csrfmiddlewaretoken)
    newtoken=csrfmiddlewaretoken[0]
    print(newtoken)
    body={
        "csrfmiddlewaretoken":newtoken,
        "username":"admin",
        "password":"yoyo123456",
        "this_is_the_login_form":"1",
        "next":"/xadmin/"

    }

    r=s.post(url,data=body,verify=False)
    print(r.text)
    return r
if __name__=="__main__":
    s=requests.session()
    mk=login_xadmin(s)
    assert "主页面 | 后台页面" in mk.text
