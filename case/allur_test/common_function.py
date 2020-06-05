import requests
import os

def login(s):
    # s=requests.session()
    url=os.environ['host']+"/SSO-SERVER/authentication/form"
    body={
        "username":"zhaolei",
          "password":"123456a",
          "loginType":"json"
        }

    r=s.post(url,json=body)
    token=r.json()['data']['tokenInfo']['token']
    print(r.json()['data']['tokenInfo']['token'])
    h={
        "Authorization":"bearer %s"%token

    }
    s.headers.update(h)
    print(s.headers)
    return r.json()


def add_buylist(s):
    url2=os.environ['host']+"/BASE-MALL-GOODS/mgt/saveBuyMallGoods.magpie"
    body={
        "oecdNo": "apec",
        "platformId": "dazong",
        "name": "国冰精制白砂糖",
        "stockNum": 99492,
        "plateCode": "buyPlate",
        "marketCode": "000",
        "situationList": [{
            "isLimitMiniExchange": "0",
            "isLimitVisibleScope": "0",
            "isChoseCus": False,
            "exchangeList": [{
                "exchangeCode": "YS20052",
                "exchangeSdt": "2020-05-26",
                "exchangeEdt": "2020-05-28",
                "exchangePrice": 0
            }],
            "price": 500,
            "priceTaxFlag": "0",
            "isLimitOrgMaxExchange": "0",
            "whFeeDate": "2020-06-07",
            "marketTipPrice": "",
            "isLimitExchange": "1",
            "situationCode": "PURCHASE_EXCESS",
            "situationName": " 超额采购 ",
            "liftingWater": {
                "areaDiffer": 0,
                "gradeDiffer": 0,
                "crushingSeasonDiffer": 0,
                "warehouseDiffer": 0,
                "qualityDiffer": 0,
                "varietyDiffer": 0,
                "brandDiffer": 0
            },
            "pricingModel": "premiumPrice",
            "priceDesc": "测试",
            "customerList": [],
            "whId": 563323076071424,
            "wmsSkuId": "36032727129309248",
            "wmsSkuCode": "86000.GUOB.R.19",
            "stockNum": 99492,
            "varietyName": "白砂糖"
        }],
        "subTitle": "测试",
        "orderNumber": 2,
        "picList": ["https://magpie-pic.oss-cn-shenzhen.aliyuncs.com/0a37899d9ed22b150835563413252cf2.png"],
        "remarks": "测试数据",
        "autoOnLineModel": "0",
        "autoOffLineModel": "0",
        "isLimitDeliveryDate": "0",
        "tagList": [],
        "plantformId": "dazong",
        "varietyCode": "101000",
        "varietyName": "白砂糖",
        "brand": "GUOB",
        "brandOrg": "BBJ000000",
        "brandOrgName": "把边江有限公司",
        "origin": "GX",
        "originName": "广西",
        "technique": "sulfuration",
        "techniqueName": "硫化",
        "brandName": "国冰",
        "grade": "R",
        "gradeName": "精制",
        "crushingSeasonName": "19/20",
        "whName": "中农网",
        "liftingWaterCeiling": 0,
        "liftingWaterFloor": 0,
        "wmsSkuCode": "86000.GUOB.R.19",
        "wmsSkuId": "36032727129309248",
        "whId": 563323076071424,
        "wmsSugarStock": 99492,
        "canUseStock": 99492,
        "areaDifferCeiling": 12,
        "areaDifferFloor": 1,
        "brandDifferCeiling": 34,
        "brandDifferFloor": 4,
        "crushingSeasonDifferCeiling": 87,
        "crushingSeasonDifferFloor": 8,
        "gradeDifferCeiling": 65,
        "gradeDifferFloor": 6,
        "qualityDifferCeiling": 67,
        "qualityDifferFloor": 7,
        "varietyDifferCeiling": 45,
        "varietyDifferFloor": 5,
        "warehouseDifferCeiling": 30,
        "warehouseDifferFloor": 3,
        "zcFeeSettleType": "HYZF",
        "yqthczSettleType": "HYZF",
        "jhType": "warehousePrice"
    }
    r2=s.post(url2,json=body)
    # print(r2.json())
    return r2.json()

def get():
    print("返回数据")




if __name__=="__main__":
    os.environ['host']="http://open.ap88.com:8900"
    s=requests.session()
    login=login(s)
    print(login)
    add_buy=add_buylist(s)
    print(add_buy)
    print(type(add_buy))
