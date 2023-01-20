
# Change Tuple Values

x = ("apple", "banana", "cherry")
y = list(x)

y[1] = "kiwi"
x = tuple(y)
print(x)

# Add items
#  1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple

y = list(x)
y.append("orange")
x = tuple(y)
print(x)

# 2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

y = ("mangos","fuck")

print(type(y))

x += y
print(x)

# Remove Items -- uples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items

y = list(x)
y.remove("apple")
x = tuple(y)
print(x)

del x
print(x)
