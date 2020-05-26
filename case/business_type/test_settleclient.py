from common.common_client import login,SettleMent_Men
from .read_yaml import yamldata
import pytest
import os
dirpath=os.path.dirname(os.path.realpath(__file__))
print(dirpath)
yamlpath=os.path.join(dirpath,"bus_bunine.yml")
print(dirpath)
data=yamldata(yamlpath)["settle_ment"]
settle_data=yamldata(yamlpath)["settlement_list"]
print(data)

@pytest.mark.skip('接口暂时出现问题')
def test_login(login_fixture):
    s=login_fixture
    r=login(s)
    assert r.json()['succeed']==True
    assert r.json()['errorMsg']== ''
    print(r)



@pytest.mark.parametrize("regSource,partFullName,userType,excepted",
                         data

                         )
def test_settlement(login_fixture,regSource,partFullName,userType,excepted):
    s=login_fixture
    settle=SettleMent_Men(s)
    c=settle.settlement()
    print("211")
    print(c.json())
    assert c.json()['succeed']==excepted['succeed']
    assert c.json()['errorMsg']==excepted['errorMsg']

@pytest.mark.parametrize("test_input,excepted",
                         settle_data
                         )
def test_settlement_list(login_fixture,test_input,excepted):
    s=login_fixture
    settle=SettleMent_Men(s)
    c=settle.settlement_list()
    print("222")
    print(c)
    assert c['succeed']==excepted['succeed']
    # assert c['errorMsg']==excepted['succeed']

@pytest.mark.webtest("ces")
class Test_send():
    def test_send_http(self):
        print("mark web test")

    def test_something_quick(self):
        print("00990")
        pass

    def test_another(self):
        print("999090")
        pass
    def test_anotherw(self):
        print("55555")
        pass

@pytest.mark.app
class Test_send_app():
    def test_send_htt(self):
        print("mark web test")

    def test_something_quic(self):
        print("00990")
        pass

    def test_anothe(self):
        print("999090")
        pass
    def test_anothers(self):
        print("55555")
        pass
