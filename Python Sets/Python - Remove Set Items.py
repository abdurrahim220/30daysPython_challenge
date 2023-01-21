thisSet = {"apple","banana","cherry"}

thisSet.remove("banana")

print(thisSet)

# Remove "banana" by using the discard() method:

thisSet.discard("apple")
print(thisSet)

thisSet = {"mango","orange","guava","jackfruit"}

x = thisSet.pop() # pop is a random remover it will remove the random index items

print(x)

print(thisSet)

# The del keyword will delete the set completely:

del thisSet
print(thisSet)