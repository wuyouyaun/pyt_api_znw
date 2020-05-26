#coding:utf-8
import yaml
import os


# file=os.path.dirname(os.path.realpath(__file__))
# yamlfile=os.path.join(file,"test.yaml")
# print(yamlfile)
# fp=open(yamlfile,"r",encoding="utf-8")
# print("1212")
# fs=fp.read()
# print(fs)
# print(type(fs))
# fss=yaml.load(fs)
# print(fss)
# print(type(fss))

# fss1=yaml.dump(fs)
# print(fss1)
# print(type(fss1))

# with open('testyaml.py',encoding="utf-8") as fp:
#     yaml.load(fp)

# y =yaml.load(yamlfile('test_yaml',"r"))
#  data = yaml.load(fs, Loader=yaml.FullLoader)
file=os.path.dirname(os.path.realpath(__file__))
yamlfile=os.path.join(file,"test.yaml")
print(yamlfile)

with open(yamlfile,"r",encoding="utf-8")as fp:
    #d=yaml.load(yamlfile)
    #c=fp.read()
    # k=fp.read()
    # print(k)
    # print("322332")
    # print(type(k))
    d=yaml.load(fp.read())
    print(d)
    print(type(d))






















