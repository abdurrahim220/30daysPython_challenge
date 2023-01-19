# Boolean Values -- Booleans represent one of two values: True or False.

# print(10>9)
# print(10 == 9)
# print(10<9)

# a = 200
# b = 33
# if a>b:
#     print("b is greater than a")
# else:
#     print("b is not greater than a")

# Evaluate Values and Variables -- The bool() function allows you to evaluate any value, and give you True or False(only return when the vlaues is empty or 0) in return

# print(bool("hello"))
# print(bool(15))

# print(bool(a))
# print(bool(b))

# class myClass():
#     def _len_(self):
#         return 0
# myobj = myClass()

# print(bool(myobj))

# Functions can Return a Boolean

def myFunction():
    return True

# print(myFunction())

if myFunction():
    print("Yes!")
else:
    print("NO!")

x = 200
print(isinstance(x,int))