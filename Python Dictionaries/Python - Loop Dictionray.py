# Loop through a Dictionary 

thisDict = {
    "name" : "rahim",
    "dob" : 1999,
    "country" : "Bangladesh"
}

for x in thisDict:
    print(x) # it will print the only key names
    print(thisDict[x]) # this will print the key : values 

# also values() --  method will return the values of the key

for x in thisDict.values():
    print(x)

# by using the keys() method to return the keys of the dictionary
for x in thisDict.keys():
    print(x)

# items() loop through the both keys : values , by using the items() method:

for x, y in thisDict.items():
    print(x,y)

