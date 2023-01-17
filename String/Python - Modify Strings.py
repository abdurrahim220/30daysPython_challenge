# Python has a set of built-in methods that you can use on strings.

# Upper Case -- The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())

# Lower Case -- The lower() method returns the string in lower case:

print(a.lower())

# Remove Whitespace -- Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

# The strip() method removes any whitespace from the beginning or the end: 

b = " Hello rahim "
print(b.strip())

# Replace String -- The replace() method replaces a string with another string:

# syntax -- replace(old_str,new_str,count) //count reffers to number how many string or word you want to replace

r = "Hello , World"
print(a.replace("H","J"))

# Split String -- The split() method returns a list where the text between the specified separator becomes the list items.

# The split() method splits the string into substrings if it finds instances of the separator:

s = "Hello, World!"
print(a.split(","))