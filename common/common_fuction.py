#coding:utf-8
import requests
#s=requests.session()
def login(s,username="test",password="123456"):
    """
    登录
    :param s:          requests.session()     参数s是requests.session()这个对象
    :param username:   账号
    :param password:   密码
    :return:s
    """
    url="http://49.235.92.12:6009/api/v1/login"
    body={
        "username":username,
        "password":password
    }
    r=s.post(url,json=body)
    print(r.text)
    token=r.json()["token"]
    print(token)
    h={
        "Content-Type":"application/json",
        "Authorization":"Token %s"%token
        }
    s.headers.update(h)
    # s.token=token
    # return token

def update_info(s,name="test",mail="283340479@qq.com",sex="F",age=20):
    """
    修改信息
    :param s: requests.session()
    :param name: 用户名
    :param mail: 邮箱
    :return:    r
    """
    url="http://49.235.92.12:6009/api/v1/userinfo"
    body={"name":name,
          "sex": sex,
          "age": age,
          "mail": mail
          }
    r1=s.post(url,json=body,verify=False)
    print(r1.json())
    return r1

def get_info(s):
    """
    查询接口
    :return: r
    """
    url="http://49.235.92.12:6009/api/v1/userinfo"
    r=s.get(url)
    return r.json()

if __name__=="__main__":
    s=requests.session()
    login(s,username="test",password="123456")
    infos=update_info(s)
    print(infos.json())
    get_in=get_info(s)
    print(get_in)
