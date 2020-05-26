import os
import yaml
# curpath=os.path.dirname(os.path.realpath(__file__))
# print(curpath)
#
# yamlpath=os.path.join(curpath,"info_dem2.yml")
# print(yamlpath)
#
# f=open(yamlpath,"r",encoding="utf-8")
# yamldata=f.read()
# print(yamldata)
#
#
# #def yamldata():
# curpath=os.path.dirname(os.path.realpath(__file__))
# print(curpath)
#
# yamlpath=os.path.join(curpath,"info_dem2.yml")
# print(yamlpath)

def yamldata(yamlpath):
    f=open(yamlpath,"r",encoding="utf-8")
    yamldata1=f.read()
    print(yamldata1)
    # print(type(yamldata))
    # 把yaml文件转换成字典
    d=yaml.load(yamldata1)
    # print(d['test_get_info'])
    #print(type(d))
    return d

def yaml_load(yamlpath1):
    fp=open(yamlpath1,"r",encoding="utf-8")
    fp1=fp.read()
    #print(fp1)
    # 将yaml文件转换成字典
    yamldata=yaml.load(fp1)
    # m=(yamldata)['test_post_info']
    # print(m)
    return yamldata
if __name__=="__main__":
    curpath=os.path.dirname(os.path.realpath(__file__))
    #print(curpath)
    yamlpath=os.path.join(curpath,"info_dem2.yml")
   # print(yamlpath)
    print(type(yamlpath))
    a=yamldata(yamlpath)#['test_get_info']
    print(type(a))




# import os
# import yaml
#
# def get_yaml_data(yamlpath):
#     '''获取yaml文件数据'''
#
#     f = open(yamlpath, "r", encoding='utf-8')
#     yamldata = f.read()
#     print(yamldata)
#
#     # 把yaml文件数据转字典
#     d = yaml.load(yamldata)
#     f.close()
#     # print(d['test_info_params'])
#     return d
#
# if __name__ == '__main__':
#     curpath = os.path.dirname(os.path.realpath(__file__))
#     print(curpath)
#     yamlpath = os.path.join(curpath, "info_dem2.yml")
#     print(yamlpath)
#     a = get_yaml_data(yamlpath)
#     print(a)
#
#















