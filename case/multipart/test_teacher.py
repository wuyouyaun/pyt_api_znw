from case.multipart.login_xadmin_page import login_xadmin
import requests
import re
from requests_toolbelt import MultipartEncoder
import pytest
from lxml import etree

from common.connet_mysql import select_sql,execute_sql
from .multipart_form_data import *

# 前置操作，新增前先清空数据
@pytest.fixture(scope="function")
def delect_teacher(login_fixture):
    '''新增老师标签前清空测试数据'''
    sql="delete  from djangoweb.hello_teacher WHERE teacher_name = '11小测试';"
    execute_sql(sql)
    yield
    print("数据清理")

def test_add_teacher(login_fixture,delect_teacher):
    '''新增老师标签'''
    s=requests.session()
    login_xadmin(s)
    # result=add_teacher_name(s)
    # sql="SELECT count(*) as a from djangoweb.hello_teacher WHERE teacher_name = '1小测试'"
    # select_result=select_sql(sql)[0]["a"]
    # print("数据库查询的结果：%s"%select_result)

    result=add_teacher_name(s)
    result_ture=add_teacher_result(result)
    print("werwefeffeefreefeeffeeef")
    print(result_ture)
    print("获取页面上返回的结果：%s"%result_ture)
    sql="SELECT count(*) as a from djangoweb.hello_teacher WHERE teacher_name = '11小测试'"
    select_result2=select_sql(sql)[0]['a']
    print(select_result2)
    assert select_result2==1


