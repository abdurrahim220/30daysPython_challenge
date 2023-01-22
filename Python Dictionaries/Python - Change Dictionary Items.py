# Change Values -- you can change the value of a specific item by referring to its key name:

thisDict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

thisDict["year"] = 2000

print(thisDict)

# Update Dictionary -- update() method will update the dictionary with the items from the given argument . 

thisDict.update({"year":2000})

print(thisDict)

