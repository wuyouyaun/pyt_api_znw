#coding:utf-8
from case.multipart.login_xadmin_page import login_xadmin
import requests
import re
from requests_toolbelt import MultipartEncoder

from lxml import etree

from common.connet_mysql import select_sql,execute_sql


def add_teacher_name(s):
    '''
    添加老师
    :param s: requests.session()
    :return: r1.text
    '''
    url = "http://49.235.92.12:8020/xadmin/hello/teacher/add/"
    r=s.get(url)
    # print(r.text)
    csrfmiddlewaretoken1=re.findall(r"value='(.+?)'",r.text)
    print(csrfmiddlewaretoken1)
    newcsrfmiddlewaretoken=csrfmiddlewaretoken1[0]
    body=MultipartEncoder(
        fields=[
            ("csrfmiddlewaretoken",'%s'%newcsrfmiddlewaretoken),
            ("csrfmiddlewaretoken",'%s'%newcsrfmiddlewaretoken),
            ("teacher_name","11小测试"),
            ("tel","185715112"),
            ("mail","353558733@qq.com"),
            ("sex",'M'),
            ("save",""),
         ]
         )
    r1=s.post(url,data=body,headers={"content-Type":body.content_type})
    return r1.text

    # s=requests.session()
    # result=add_teacher_name(s)


def add_teacher_result(result):
    '''
    添加老师的结果
    :param result: 添加老师页面返回的结果页面
    :return:
    '''
    demo=etree.HTML(result) # 调用html解析库，返回txt文本，解析html
    nodes=demo.xpath('//*[@id="changelist-form"]/div[1]/table/tbody/tr[1]/td[2]/a')#通过xpath找到节点
    print(nodes[0])  #调用xpath解析，获取元素对象
    # 通过对象可以获取属性
    get_result=nodes[0].text
    return get_result

def add_upload_pictures(s):
    '''
    添加图片
    :param result: 添加图片后返回的字符串类型的html文本
    :return: 返回的页面元素结果
    '''

    url="http://49.235.92.12:8020/xadmin/hello/uploadimage/add/"
    r=s.get(url)
        # print(r.text)
    csrfmiddlewaretoken1=re.findall(r"value='(.+?)'",r.text)
    print(csrfmiddlewaretoken1)
    newcsrfmiddlewaretoken=csrfmiddlewaretoken1[0]
    # print(newcsrfmiddlewaretoken)
    body=MultipartEncoder(
        fields=[
            ("csrfmiddlewaretoken","%s"%newcsrfmiddlewaretoken),
            ("csrfmiddlewaretoken","%s"%newcsrfmiddlewaretoken),
            ("name","测试3338"),
            ("image",('5666.png',open(r'C:\Users\Administrator\Desktop\5666.png',"rb"),"image/png")),
            ("add_time_0","2020/06/01"),
            ("add_time_1","16:58"),
            ("initial-add_time_0","2020/05/29"),
            ("initial-add_time_1","16:58"),
            ("save",""),
            ]
    )
    # print("ewreerwrewrewrewqqqqqqqqq54333333333")
    r2=s.post(url,data=body,headers={"content-Type":body.content_type})
    # print(r2.text)
    return r2.text
    # text=r2.text
def add_upload_pictures_result(text):
    '''判断添加图片结果'''
    print("11111111111111111111111111111111111")
    demo=etree.HTML(text)
    nodes=demo.xpath('//*[@id="changelist-form"]/div[1]/table/tbody/tr[1]/td[2]/a')
    # print(nodes[0])
    get_result = nodes[0].text
    # print(get_result)
    return get_result

# def add_file_image():
#     '''添加文件和图片'''

s=requests.session()
login_xadmin(s)
url3="http://49.235.92.12:8020/xadmin/hello/fileimage/add/"
r=s.get(url3)

csrfmiddlewaretoken=re.findall(r"value='(.+?)'",r.text)
print(csrfmiddlewaretoken)
body1=MultipartEncoder(
    fields=[
        ("csrfmiddlewaretoken",csrfmiddlewaretoken[0]),
        ("csrfmiddlewaretoken",csrfmiddlewaretoken[0]),
        ("title","测试小脚本1"),
        ("image",("5666.png",open(r'C:\Users\Administrator\Desktop\5666.png',"rb"),"image/png")),
        ("fiels",("ce12.txt",open(r'C:\Users\Administrator\Desktop\ce12.txt',"rb"),"text/plain")),
        ("_save","")
        ]
        )
print("345453443453435435434343")
r3=s.post(url=url3,data=body1,headers={"content-Type":body1.content_type})
print(r3.text)

demo=etree.HTML(r3.text)
result_demo=demo.xpath('//*[@id="changelist-form"]/div[1]/table/tbody/tr[1]/td[2]/a')
print(result_demo[0])
result_get=result_demo[0].text
print(result_get)
assert result_get=="测试小脚本1"
# s=requests.session()
# login_xadmin(s)


















# if __name__=="__main__":
#     s=requests.session()
#     login_xadmin(s)
    # kl=add_upload_pictures(s)
    # print(kl)
    # result=add_upload_pictures_result(kl)
    # print(result)
    # assert result=="测试3338"































def add_file_image():
    '''添加文件和图片'''
    # s=requests.session()
    # login_xadmin(s)
    url3="http://49.235.92.12:8020/xadmin/hello/fileimage/add/"
    r=s.get(url3)

    csrfmiddlewaretoken=re.findall(r"value='(.+?)'",r.text)
    print(csrfmiddlewaretoken)
    body1=MultipartEncoder(
        fields=[
            ("csrfmiddlewaretoken",csrfmiddlewaretoken[0]),
            ("csrfmiddlewaretoken",csrfmiddlewaretoken[0]),
            ("title","测试小脚本1"),
            ("image",("5666.png",open(r'C:\Users\Administrator\Desktop\5666.png',"rb"),"image/png")),
            ("fiels",("ce12.txt",open(r'C:\Users\Administrator\Desktop\ce12.txt',"rb"),"text/plain")),
            ("_save","")
            ]
            )
    print("345453443453435435434343")
    r3=s.post(url=url3,data=body1,headers={"content-Type":body1.content_type})
    print(r3.text)











# if __name__=="__main__":
#     s=requests.session()
#     login_xadmin(s)
#     # result=add_teacher_name(s)
#     sql="SELECT count(*) as a from djangoweb.hello_teacher WHERE teacher_name = '11小测试'"
#     select_result=select_sql(sql)[0]["a"]
#     print(select_result)
#     print("数据库查询的结果：%s"%select_result)
#     # print(select_result)
#     # result_ture=add_teacher_result(result)
#     # print("获取页面上返回的结果：%s"%result_ture)
#     # assert result_ture=="1小测试"
#     # sql1="delete  from djangoweb.hello_teacher WHERE teacher_name = '1小测试';"
#     # execute_result=execute_sql(sql1)
#     # print("数据库查询的结果：%s"%execute_result)
#     result=add_teacher_name(s)
#     result_ture=add_teacher_result(result)
#     print("获取页面上返回的结果：%s"%result_ture)
#     select_result2=select_sql(sql)[0]['a']
#     print(select_result2)
#     assert select_result2-select_result==1      # 通过数据库返回的结果去断言，也可以通过接口去断言
#
#









