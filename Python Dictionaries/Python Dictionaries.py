# Dictionary -- Dictionaries are used to store data values in key:value pairs.
# Dictionary Items - Data Types -- The values in dictionary items can be of any data type:


thisDict = {
    "brand": "Ford",
    "model": "Mustang",  # Dictionary Items
    "year": 1964,
    "year": 2737,  # duplicates not allow
    "color": ["red", "yellow", "green"],
    "fruits": {"apple", "mangos"}

}

print(thisDict)
print(len(thisDict))  # Dictionary Length
print(thisDict["brand"])

# The dict() Constructor -- It is also possible to use the dict() constructor to make a dictionary.

thisConst = dict(brand="Ford",
                 model="Mustang",  # Dictionary Items
                 year=1964,

                 color=["red", "yellow", "green"],
                 fruits={"apple", "mangos"})
print(thisConst)
