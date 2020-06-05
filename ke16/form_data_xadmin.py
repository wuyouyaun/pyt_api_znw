from ke15.login_xadmin_page import login_xadmin
from requests_toolbelt import MultipartEncoder
import requests
import re
from lxml import etree
import os


def add_teacher_name(s):
    # 添加老师页面
    url = os.environ["host"]+"/xadmin/hello/teacherman/add/"
    # 获取页面隐藏参数
    r = s.get(url)
    # print(r.text)

    csrftoken = re.findall("name='csrfmiddlewaretoken' value='(.+?)'", r.text)
    print(csrftoken)

    body = MultipartEncoder(fields=[
                                    ("csrfmiddlewaretoken", csrftoken[0]),
                                    ("csrfmiddlewaretoken", csrftoken[0]),
                                    ("teacher_name", "yoyo333"),
                                    ("tel", "122222222"),
                                    ("mail", "1111@qq.com"),
                                    ("sex", "M"),
                                    ("_save", "")
                                ]
                                )

    r2 = s.post(url, data=body, headers={"content-Type": body.content_type})
    # print(r2.text)
    return r2.text


def get_add_result(text):
    demo = etree.HTML(text)
    nodes = demo.xpath('//*[@id="changelist-form"]/div[1]/table/tbody/tr[1]/td[2]/a')
    print(nodes[0])  # 元素对象
    # 通过元素对象获取属性
    get_result = nodes[0].text
    print("获取页面返回结果：%s"%get_result)
    return get_result


# s = requests.session()
# login_xadmin(s)
#
# url3 = "http://49.235.92.12:8020/xadmin/hello/fileimage/add/"
# r = s.get(url3)
# # print(r.text)
#
#
# csrftoken = re.findall("name='csrfmiddlewaretoken' value='(.+?)'", r.text)
# print(csrftoken)
# body3 = MultipartEncoder(
#     fields=[
#         ("csrfmiddlewaretoken", csrftoken[0]),
#         ("csrfmiddlewaretoken", csrftoken[0]),
#         ("title", "上传图片测试111"),
#         ("image", ""),
#         ("fiels", ("122.png", open("D:\\122.png", "rb"), "image/png")),
#         ("_save", "")
#
#     ]
# )
# r3 = s.post(url3, data=body3,
#             headers={"content-Type": body3.content_type})
# print(r3.text)







# if __name__ == '__main__':
#     s = requests.session()
#     login_xadmin(s)
#     from ke12.connet_mysql import select_sql
#     sql = "SELECT count(*) as sum from djangoweb.hello_teacher WHERE teacher_name = 'yoyo333'"
#     result1 = select_sql(sql)[0]["sum"]
#     print("查询结果：%s" % result1)
#     text = add_teacher_name(s)
#     result2 = select_sql(sql)[0]["sum"]
#     print("查询结果：%s" % result2)
#     assert result2-result1 == 1
#     # result = get_add_result(text)
#     # assert result == "yoyo333"
