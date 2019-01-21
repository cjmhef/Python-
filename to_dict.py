fruit = {"one": "apple",
         "two": "pear",
         "three": "grape",
         "four": "watermelon",
         "five": "banana"
}
print(fruit)
print(fruit["two"])  # find a value by key ,key as the index
#  and key-value
fruit["six"] = "peach"
print(fruit)
del fruit["six"]
print(fruit)
fruit.clear()
print(fruit)
del fruit
print(fruit)