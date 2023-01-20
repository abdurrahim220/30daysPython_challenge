# Access Tuple items

thistuple = ("apple","banana","cherry","mango","blackberry","jackfruit")
print(thistuple[2])

# Negative Indexing

print(thistuple[-1])

# Range of Indexes

print(thistuple[2:5])
print(thistuple[2:]) # start to end
print(thistuple[:3]) # end to start


# Range of Negative Indexes

print(thistuple[-4:-1])


# Check if Item Exists

if "apple" in thistuple:
    print("Yes,search is in the furit tuple")
else:
    print("No,search index is not in the furit tuple")