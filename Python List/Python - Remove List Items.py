# Remove Specified Item -- The remove() method removes the specified item

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index -- The pop() method removes the specified index.

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist.pop()
print(thislist) # f you do not specify the index, the pop() method removes the last item.

# The del keyword also removes the specified index:
# del thislist[0]
# print(thislist) 

# The del keyword can also delete the list completely.
# del thislist
# print(thislist)  #it will show some error text

# Clear the List -- The clear() method empties the list.

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)