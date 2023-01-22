# Removing items 
# pop metod removes the items with the specified key name:
thisDict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1667
}

thisDict.pop("model")
print(thisDict)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisDict.popitem()
print(thisDict)

# the del keyword removes the item with the specified key name:

del thisDict["brand"]

print(thisDict)

# the del keyword can also delete the dictionary completely:

# del thisDict
print(thisDict) # this will cause an error because "thisDict" no longer exit

thisDict.clear() # this method will empties the entire dictionary 
print(thisDict)