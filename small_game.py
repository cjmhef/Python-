import random
number = random.randint(0,100)
content = int(input("please input a number:"))
while number != content:
    if content > number:
        content = int(input("your number is bigger,please input a smaller number:"))
    elif content < number:
        content = int(input("your number is smaller,please input a bigger number:"))
print("congratulation!")
