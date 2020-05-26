from case.business_type.buy_business import buy_list
from .read_yaml import yamldata
import requests
import pytest
import os

dirpath=os.path.dirname(os.path.realpath(__file__))
print(dirpath)
yamlpath=os.path.join(dirpath,"bus_bunine.yml")
print(dirpath)
data=yamldata(yamlpath)['bus_type']
print(data)

@pytest.mark.parametrize("mallPlate,pricingModel,bdPremiumPrice,bdnPremiumPriceCeiling,bdPremiumPriceFloor,limitChoosePositionDate,expected",
                          data,

                          # ids=["测试标题1，"
                          #      ]
                          )
def test_BuyBuniness(unlogin_fixture,mallPlate,pricingModel,bdPremiumPrice,bdnPremiumPriceCeiling,
                     bdPremiumPriceFloor,limitChoosePositionDate,expected):
    print("2222")
    s=unlogin_fixture
    buydata=buy_list(s,mallPlate=mallPlate,pricingModel=pricingModel,bdPremiumPrice=bdPremiumPrice,
             bdnPremiumPriceCeiling=bdnPremiumPriceCeiling,bdPremiumPriceFloor=bdPremiumPriceFloor,limitChoosePositionDate=limitChoosePositionDate)
    assert buydata['succeed']==expected["succeed"]
    assert buydata['errorMsg'] ==expected["errorMsg"]
