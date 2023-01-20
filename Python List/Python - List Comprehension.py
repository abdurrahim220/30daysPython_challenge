# List Comprehension -- 


# without comprehension

fruits = ["mango","jackfruit","blackberry","pineapple","banana","litchi","lemon","guava","berry","papaya"]

# newlist = []

# for x in fruits:
#     if "a" in x:
#         newlist.append(x)

# print(newlist)

newlist = [x for x in fruits if "b" in x]
print(newlist)

# The Syntax -- newlist = [expression for item in iterable if condition == True]

# Condition -- The condition is like a filter that only accepts the items that valuate to True.

newlist = [x for x in fruits if x != "banana"]
print(newlist)

newlist = [x for x in fruits] #it will show the whole list or array
print(newlist)
# Expression
newlist = [x.upper() for x in fruits]
print(newlist)

# newlist = ["hello" for x in fruits]
# print(newlist) # i can set the outcome from the list or outcome

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

# The expression in the example above says:

# "Return the item if it is not banana, if it is banana return orange".


# Iterable = The iterable can be any iterable object, like a list, tuple, set etc.
newlist = [x for x in range(15)]
print(newlist) 

newlist = [x for x in range(10) if x < 5]

print(newlist)
