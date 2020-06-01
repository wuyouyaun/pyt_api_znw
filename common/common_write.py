#coding:utf-8

# filename="programe.txt"

#with open(filename,"w",encoding="utf-8")as fp:
#    fp.write("1效验测试数据\n")
#    fp.write("2效验测试数据\n")

# with open(filename,"a",encoding="utf-8")as fp:
#     fp.write("3效验测试数据\n")
#     fp.write("4效验测试数据\n")

# with open(filename,encoding="utf-8")as ff:
#     lines=ff.readlines()
#     print(lines)
#     for line in lines:
#         print(line)
#
# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.rstrip()
# print(pi_string)
# print(len(pi_string))

# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())

# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     for line in file_object:
#         print(line)
filename = 'pi_digits.txt'
with open("pi_digits.txt",encoding="utf-8")as ff:
    lines=ff.readlines()
    print(lines)
pi_string=""
for line in lines:
    print(line.rstrip())
    pi_string+=line.rstrip()
print(pi_string)
print(len(pi_string))
