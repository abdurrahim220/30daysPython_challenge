# Add Items -- To add one item to a set use the add() method.

thisSet = {"apple","banana","cherry"}

thisSet.add("orange")

print(thisSet)

# Add Any Iterable -- The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

myList = ["kiwi","orange"]

thisSet.update(myList)
print(thisSet)

