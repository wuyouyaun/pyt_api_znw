import requests
def login(s):
    url="http://seedtest.ap-ec.cn/SSO-SERVER/app/token"
    body={
           "grant_type":"password",
           "loginType":"json",
           "marketId":"000",
           "password":"123456a",
           "scope":"all",
           "username":"200010"
           }
    #s=requests.session()
    r=s.post(url,json=body,verify=False)
    print(r.json())
    token=r.json()["data"]['tokenInfo']['token']
    # s.headers.update(token)
    # print(s.headers)
    h={
        "Content-Type":"application/json",
        "Authorization":"bearer %s"%token
    }
    s.headers.update(h)
    print(s.headers)
    return r


class SettleMent_Men():
    def __init__(self,s:requests.session):
        self.s=s

    def settlement(self,regSource="1",partFullName="刘二畅2",userType="mchtType02"):
        url="http://192.168.11.198:30005/pcuser-service-lc/appClient/applyDeliveryUser.magpie"
        body={
          "regSource":regSource ,
          "partFullName":partFullName,
          "userType":userType,
          "remark":"",
          "authMobile":"",
          "certNo":"",
          "bank":"",
          "bankNo":"",
          "cardImgFront":"",
          "cardImgBack":"",
          "creditCodeCard":"",
          "cardImgBiz":"",
          "legalRepr":"",
          "legalReprPhone":"",
          "legalReprId": "",
          "foodCirculationLicense":"",
          "billContact":"",
          "billAddress":"",
          "billBank":"",
          "billBankNo": ""
             }
        r=self.s.post(url,json=body,verify=False)
        return r

    def settlement_list(self):
        url="http://192.168.11.198:30005/pcuser-service-lc/appClient/deliveryUserList.magpie"
        body={"":"3"
                }
        r=self.s.post(url,json=body)
        return r.json()

if __name__=="__main__":
    s=requests.session()
    url="http://seedtest.ap-ec.cn/SSO-SERVER/app/token"
    c=login(s)
    print(c.json())
    print("1111111")
    r1=SettleMent_Men(s)
    b=r1.settlement()
    print (b.json())
    r2=SettleMent_Men(s)
    c=r2.settlement_list()
    print("34443")
    print (c)


























