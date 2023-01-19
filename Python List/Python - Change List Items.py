# Change Item Value -- To change the value of a specific item, refer to the index number:

thislist = ["apple","banana","chery"]

print(thislist)

thislist[1] = "mangos"
thislist[-1] = "orange"

print(thislist)

# Change a Range of Item Values -- To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values

thislist = ["apple","banana","chery","mangos","orange","jackfruit"]

print(thislist)

thislist[2:6] = "royal","rafik","masuma","mowe"

print(thislist)

# Insert Items -- To insert a new list item, without replacing any of the existing values, we can use the insert() method.

thislist.insert(2,"watermelon")
print(thislist)