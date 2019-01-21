# coding=utf-8
content = input("please input content:")
print("the content is:%r" %content)  # use %r rather than %d、%s
str = "hello\nworld"  # escape character\implement a newline
print(str)
toif = open("F:\\python\\Python_tuday\\toif.py" , "r",encoding="utf-8")
print("\n".join(toif.readlines()))  # escape character \\
print("my name is \"chenjinmei\"\'se\'")  # escape character \\ deal with special char
# array practice
fruit = ["apple","watermelon","pear","nut"]  # create array
print(len(fruit))
print(fruit, fruit[1])
