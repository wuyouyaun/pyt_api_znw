from common.common_fuction import login,update_info,get_info
import  pytest
import os
from common.common_cls import Userinfo
import requests
from common.read_yaml import yamldata
curpath=os.path.dirname(os.path.realpath(__file__))
print(curpath)
yamlpath=os.path.join(curpath,"info_dem2.yml")
test_yam=yamldata(yamlpath)['test_get_info']
print(type(test_yam))
print(test_yam)
@pytest.mark.skip("待开发")
def test_02():
    """这个接口还未开发"""
    print("该接口未开发完成，有缺陷")
# def test_4(login_fixture):
#     print("21111")

# test_datas=[
#                         ("F",{'message': 'update some data!', 'code': 0}),
#                         ("M",{'message': 'update some data!', 'code': 0}),
#                         ("V",{'message': '参数类型错误', 'code': 3333})
#                          ]
# class test_info():
#     def __init__(self,s):
#         self.s=s
#
#         print("111")

    # def test_02():
    # """这个接口还未开发"""
    # print("该接口未开发完成，有缺陷")

@pytest.mark.parametrize("sex,age,expected",
                        test_yam,
                         ids=[                                 # ids给用例添加一个标题
                             "修改个人信息sex=M,成功",
                             "修改个人信息sex=F,成功",
                             "修改个人信息sex=V,异常场景"
                         ]
                          )
def test_get_info(login_fixture,sex,age,expected):

    """测试修改个人信息接口"""
    #s=requests.session()
    print("\n用例")
    # login(s)  # 登录
    s=login_fixture
    #print(s.headers)
    # if not s.headers.get('Authorization',""):
    #     pytest.skip("跳过后面的用例")
    # infos=Userinfo(s)  #实例化
    # infos.update_info()
    #infos=Userinfo(s)
    infos=Userinfo(login_fixture)
    print("1212")
    info=infos.update_info()
    print(info.json())
    # info1=infos.get_info()
    # print(info1)
  #修改
    print("2233")
    print(infos)
    print(type(infos))

    assert info.json()['message']==expected['message']
    assert info.json()['code']==expected['code']
#

def test_3(login_fixture):
    print("\n11111")


# @pytest.mark.test_demo
# def test_4(login_fixture):
#     print("\n"+"21111")
# @pytest.mark.test_demo
# def test_5(login_fixture):
#     print("xxx模块 自动化用例")
