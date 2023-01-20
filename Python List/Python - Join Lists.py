# Join Two Lists 
# # One of the easiest ways are by using the + operator.

list1 = [1,2,3,4,5]
list2 = ["a","b","c"]

# two_join = list1 + list2
# print(two_join)

# Another way to join two lists is by appending all the items from list2 into list1, one by one:

for x in list2:
    list1.append(x)

print(list1)

# Or you can use the extend() method, which purpose is to add elements from one list to another list:

list1.extend(list2)
print(list1)