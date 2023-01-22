# Copy a Dictionary -- You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

# There are ways to make a copy, one way is to use the built-in Dictionary method copy().

thisDict = {
    "name" : "Ford",
    "model" :"Mi a1",
    "dob" : 2017
}

myDict = thisDict.copy()

print(myDict)

# Another way to make a copy is to use the built-in function dict().

myDict1 = dict(thisDict)
print(myDict1)