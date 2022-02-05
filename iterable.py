fruits = ["apple", "lemon", "peach"]

# リストはiteratorではない
# print(next(fruits))

fruits_iterator = iter(fruits)
print(next(fruits_iterator))
print(iter(fruits_iterator))

print("*" * 30)
print(next(fruits_iterator))
print(fruits_iterator.__next__())
