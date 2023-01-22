# Accessing Items -- you can access the items of a dictionary by referring to its key name , inside square brackets:

thisDict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1994
}

x = thisDict["model"]
print(x)

# There is also a method called get() that will give you the same result:

x = thisDict.get("brand")
print(x)

# Get Keys -- the keys() method will return a list of all the keys in the dictionary

x = thisDict.keys()
print(x)

# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

thisDict["color"] = "white"

print(x)

# Get Values -- The values() method will return a list of all the values in the dictionary.

x = thisDict.values()
print(x)

thisDict["rahim"] = "student"
print(x)

# Get Items -- the items() method will return each items in a dictionary ,as tuples list.

x = thisDict.items()
print(x)

thisDict["dob"] = 1999

print(x)


# check if exits 
if "model" in thisDict:
    print("yes")
else:
    print("no")