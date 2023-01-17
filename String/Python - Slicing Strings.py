# Python - Slicing Strings -- You can return a range of characters by using the slice syntax.

# Specify the start index and the end index, separated by a colon, to return a part of the string.

# get the character from position 2 to position 5:

b = "Hello World"

b = "Rahim"

print(b[2:5])

# Slice From the Start -- [start is 0:eng number ]

print(b[:5])

# Slice To the End  -- [start num : end is not define]

print(b[2:])

# Negative Indexing -- Use negative indexes to start the slice from the end of the string:
'''
Example
Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):

'''

b = "Hello, World!"
print(b[-5:-3])