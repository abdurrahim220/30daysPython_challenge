'''
List
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:

'''

thislist = ["apple","banana","cherry"]
print(thislist)
print(thislist[2])

# List Items -- List items are ordered, changeable, and allow duplicate values.

# Ordered -- When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

# If you add new items to a list, the new items will be placed at the end of the list.

# Changeable -- The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

# Allow Duplicates -- Since lists are indexed, lists can have items with the same value:

thislist = ["apple","apple","cherry","banana","cherry"]

print(thislist)
print(len(thislist)) #list of the length
print(type(thislist)) #list type

# List Items - Data Types -- this can be any data types
# also a list contain different data types

list1 = ["apple","apple","cherry","banana","cherry"]
list2 = [1,2,3,4,5]
list3 = [True,False,False]
list4 = ["abc",34,True,40,"Male"]

# The list() Constructor -- It is also possible to use the list() constructor when creating a new list. 

thislist = list(("apple","banana","cherry","novel"))
print(thislist)



