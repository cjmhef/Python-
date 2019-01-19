#  读取键盘输入和if语句
a = input("请输入数字：")
num = int(a)  # input(0)输入的内容数据类型是str，所以注意要加上int()
if num == 3:
    print("你好！")
elif num == 4:
    print("欢迎光临")
elif num == 1:
    print("早上好")
else:
    print("输入有误")
print(type(num))
print(type(a))
