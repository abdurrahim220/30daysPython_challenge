# Loop Through a List -- You can loop through the list items by using a for loop:

t_l = ["apple","banana","cherry"]

for x in t_l:
    print(x)

# Loop Through the Index Numbers -- Use the range() and len() functions to create a suitable iterable

for i in range(len(t_l)):
    print(t_l[i])


# Using a While Loop -- Use the len() function to determine the lenght of the list, then start at 0 and loop your way through the list items by referring their indexes.

# Remember to increase the index by 1 after each iteration.

i = 0
while i<len(t_l):
    print(t_l[i])
    i += 1

# Looping Using List Comprehension -- A short hand for loop that will print all items in a list:

[print(x) for x in t_l]