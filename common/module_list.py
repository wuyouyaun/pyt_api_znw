# print(5/0)

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("division by zero")


# d=["吴有源"]
# m=5
# name=input("请输入您的用户名：")
# if name in d:
#     password=input("请输入您的密码：")
#     if d[0]==password:
#         print("登陆成功")
#     else:
#         m-=1
#         print("你输入的密码有误,，还有%s次机会"%m)
#         continue
# else:
#     print ("你输入的用户名不正确")
# d=["吴有源"]
# m=5
# while True:
# 	password = input('请输入您的密码：')
# 	if d[0] == password:
# 		print('进入系统')
# 		break
#     else:
#         m-=1
#         print('您输入的密码不正确，还有%s次机会'%m)
#         continue






#
#
# d = ["吴有源"]
# m = 5
# while True:
#     name = input('请输入您的用户名：')
#     if name in d:
#         break
#     else:
#         print('您输入的用户名不存在，请重新输入')
#         continue
#
# while 1:
#     password = input('请输入您的密码：')
#     if d[0] == password:
#         print('进入系统')
#         break
#     else:
#         m -= 1
#         if m > 0:
#             # if m<=0:
#             print('您输入的密码不正确，还有{}次输入机会'.format(m))
#         if m <= 0:
#             print('您输入的密码次数超过次数')
#         continue


print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:answer = int(first_number) / int(second_number)
    except ZeroDivisionError: print("You can't divide by 0!")
    else:print(answer)
