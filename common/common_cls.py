import requests
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
class Userinfo():
    """个人信息"""
    def __init__(self,s:requests.session):
        self.s=s

    def update_info(self,name="test",mail="283340479@qq.com",sex="F",age="21"):
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
        r=self.s.post(url,json=body)
        return r

    def get_info(self):
        """
        查询接口
        :return: r
        """
        url="http://49.235.92.12:6009/api/v1/userinfo"
        r=self.s.get(url)
        return r.json()

if __name__=="__main__":
    s=requests.session()
    #先登录
    login(s)

    info=Userinfo(s)  #实例化
    ml=info.update_info()
    print(ml.json())
    mk=info.get_info()
    print(mk)
