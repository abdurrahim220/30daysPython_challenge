# Access Items -- List items are indexed and you can access them by referring to the index number:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])


# Negative Indexing -- -1 refers to the last item, -2 refers to the second last item etc.

thislist = ["apple", "banana", "cherry","orange", "kiwi", "melon", "mango"]
print(thislist[-1])
print(thislist[-4:-1])


# Range of Indexes -- You can specify a range of indexes by specifying where to start and where to end the range.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[3:6])
print(thislist[:6]) #it will not show the lust item
print(thislist[3:]) #start to end

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

