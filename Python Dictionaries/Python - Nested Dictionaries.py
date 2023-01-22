# Nested Dictionaries -- a dictionary can contain dictionaries , this is called nested dictionaries

myFamily = {
    "chid1": {
        "name": "Rafik",
        "year": 1996
    },
    "child2": {
        "name": "Rahim",
        "year": 1999
    },
    "Child3": {
        "name": "Masuma",
        "year": 2004
    }
}

print(myFamily)


chid1 = {
    "name": "Rafik",
    "year": 1996
}

child2 = {
    "name": "Rahim",
    "year": 1999
}

Child3 = {
    "name": "Masuma",
    "year": 2004
}

myFamily2 = {"child1": chid1,
             "child2": child2,
             "child3": Child3,
             }
print(myFamily2)