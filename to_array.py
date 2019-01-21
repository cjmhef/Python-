#  study array's property
fruit = ["pear","apple","watermelon", "nut"]
# append()
fruit.append("peach")
print(fruit)
# insert(index,element)
fruit.insert(2,"grape")
print(fruit)
# alter element
fruit[2] = "banana"
print(fruit)
# delete element
fruit.pop()  # delete the last element
print(fruit)
fruit.pop(2)  # delete the specified element
print(fruit)
