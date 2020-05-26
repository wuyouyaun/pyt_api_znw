import os
import requests
import yaml

def yamldata(yamlpath):
    # dirpath=os.path.dirname(os.path.realpath(__file__))
    # print(dirpath)
    # yamlpath=os.path.join(dirpath,"bus_bunine.yml")
    # print(dirpath)

    fp=open(yamlpath,"r",encoding="utf-8")
    yamldata=fp.read()
    # print(yamldata)
    # print(type(yamldata))

    yamlda=yaml.load(yamldata)
    # print(yamlda)
    return yamlda


if __name__=="__main__":
    dirpath=os.path.dirname(os.path.realpath(__file__))
    print(dirpath)
    yamlpath=os.path.join(dirpath,"bus_bunine.yml")
    print(dirpath)
    data=yamldata(yamlpath)['settle_ment']
    print(data)
