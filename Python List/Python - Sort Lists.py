# Sort List Alphanumerically -- ist objects have a sort() method that will sort the list alphanumerically, ascending, by default:

fruits = ["mango","jackfruit","blackberry","pineapple","banana","litchi","lemon","guava","berry","papaya"]

fruits.sort()
print(fruits)


list_number = [1,2,3,4,5,3,5,4654,65,65,15,86,98,632,6,8,6546,5498,4,654,984,69865,48,5416,574,4,654]

list_number.sort()
print(list_number)

# Sort Descending -- To sort descending, use the keyword argument reverse = True:

fruits.sort(reverse=True)

print(fruits)

list_number.sort(reverse=True)
print(list_number)

# Customize Sort Function -- You can also customize your own function by using the keyword argument key = function.

def myfuction(n):
    return abs(n-50)

thislist = [100,20,30,50,40,45,35,65,55,78,12,61,79,68,85,83,90]

thislist.sort(key=myfuction)
print(thislist)

# Case Insensitive Sort -- By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Reverse Order -- The reverse() method reverses the current sorting order of the elements.

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


