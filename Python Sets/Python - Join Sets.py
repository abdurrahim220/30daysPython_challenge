#  Join two sets 
#  union() -- The union() method returns a new set with all items from both sets:
#  update() -- The update() method inserts the items in set2 into set1:

set1 = {"a","b","c","d"}
set2 = {1,2,3,4,5}

set3 = set1.union(set2)

print(set3)

set3.update(set1)

print(set3)

# Keep ONLY the Duplicates -- The intersection_update() method will keep only the items that are present in both sets.

x = {"google","banana","cherry","apple"}
y = {"google","microsoft","apple"}

x.intersection_update(y)

y.intersection(x) #The intersection() method will return a new set, that only contains the items that are present in both sets.

print(x)
print(y)

# Keep All, But NOT the Duplicates -- The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

x.symmetric_difference_update(y)
print(x)

# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

y.symmetric_difference(x)
print(y)

