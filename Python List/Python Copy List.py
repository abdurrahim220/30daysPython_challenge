# Copy a List -- You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
# There are ways to make a copy, one way is to use the built-in List method copy(). or list(name).

fruits = ["mango","jackfruit","blackberry","pineapple","banana","litchi","lemon","guava","berry","papaya"]

myfruit = fruits.copy()

list_fruit = list(fruits)

print(myfruit)
print(list_fruit)