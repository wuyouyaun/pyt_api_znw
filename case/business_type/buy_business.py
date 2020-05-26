import requests

def buy_list(s,mallPlate,pricingModel,bdPremiumPrice,
             bdnPremiumPriceCeiling,bdPremiumPriceFloor,limitChoosePositionDate):
    url="http://192.168.7.162:16031/mgtshowgroup/setObjectVal"
    body={
        "formJSON": {
            "id": "35661400904667200",
            "showGroupObjectModel": "situationMarket",
            "mallPlate": mallPlate,
            "pricingModel": pricingModel,
            "bdPremiumPrice": bdPremiumPrice,
            "bdnPremiumPriceCeiling": bdnPremiumPriceCeiling,
            "bdPremiumPriceFloor": bdPremiumPriceFloor,
            "limitChoosePositionDate":limitChoosePositionDate
        },
        "requestAttrMap": {
            "userNo": "zhangsan"
        }
    }
    # s=requests.session()
    r=s.post(url,json=body)
    #print(r.json())
    return r.json()


def sell_list(s,mallPlate,pricingModel,bdPremiumPrice,
             bdnPremiumPriceCeiling,bdPremiumPriceFloor,limitChoosePositionDate):
    url="http://192.168.7.162:16031/mgtshowgroup/setObjectVal"
    body={
        "formJSON": {
            "id": "35661400904667200",
            "showGroupObjectModel": "situationMarket",
            "mallPlate": mallPlate,
            "pricingModel": pricingModel,
            "bdPremiumPrice": bdPremiumPrice,
            "bdnPremiumPriceCeiling": bdnPremiumPriceCeiling,
            "bdPremiumPriceFloor": bdPremiumPriceFloor,
            "limitChoosePositionDate":limitChoosePositionDate
        },
        "requestAttrMap": {
            "userNo": "zhangsan"
        }
    }
    # s=requests.session()
    r=s.post(url,json=body)
    #print(r.json())
    return r.json()



if __name__=="__main__":
    s=requests.session()
    re=buy_list(s,mallPlate="buyPlate",pricingModel="premiumPrice",bdPremiumPrice=500,
             bdnPremiumPriceCeiling=100,bdPremiumPriceFloor=-100,limitChoosePositionDate=4)
    print(re)
    re1=buy_list(s,mallPlate="",pricingModel="premiumPrice",bdPremiumPrice=500,
             bdnPremiumPriceCeiling=100,bdPremiumPriceFloor=-100,limitChoosePositionDate=4)
    print(re1)
    re=buy_list(s,mallPlate="buyPlate",pricingModel="premiumPrice",bdPremiumPrice=500,
             bdnPremiumPriceCeiling=100,bdPremiumPriceFloor=-100,limitChoosePositionDate=4)
    print(re)
    re=buy_list(s,mallPlate="buyPlate",pricingModel="premiumPrice",bdPremiumPrice="",
             bdnPremiumPriceCeiling=100,bdPremiumPriceFloor=-100,limitChoosePositionDate=4)
    print(re)
    re=buy_list(s,mallPlate="buyPlate",pricingModel="premiumPrice",bdPremiumPrice=500,
             bdnPremiumPriceCeiling="",bdPremiumPriceFloor=-100,limitChoosePositionDate=4)
    print(re)
    re=buy_list(s,mallPlate="buyPlate",pricingModel="premiumPrice",bdPremiumPrice=500,
             bdnPremiumPriceCeiling=100,bdPremiumPriceFloor="",limitChoosePositionDate=4)
    print(re)
    re=buy_list(s,mallPlate="buyPlate",pricingModel="premiumPrice",bdPremiumPrice="500",
             bdnPremiumPriceCeiling=100,bdPremiumPriceFloor=-100,limitChoosePositionDate="")
    print(re)
    re=buy_list(s,mallPlate="11",pricingModel="11",bdPremiumPrice="500",
             bdnPremiumPriceCeiling="cvb",bdPremiumPriceFloor=-100,limitChoosePositionDate="")
    print(re)