# Strings -- Strings in python are surrounded by either single quotation marks, or double quotation marks.

# 'hello' is the same as "hello"

print("Hello World!")
print('Hello World!')

# Assign String to a Variable -- Assigning a string to a variable is done with the variable name followed by an equal sign and the string:Or three single quotes:

a = "hello"
print(a)

# Multiline Strings -- You can assign a multiline string to a variable by using three quotes:

a = '''My name is abdur rahim. Now i am writting python language in visual studio code'''

print(a)

#  Strings are Arrays -- Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

# However, Python does not have a character data type, a single character is simply a string with a length of 1.

# Square brackets can be used to access elements of the string.

b = "Hello World"

print(b[1])
print()
# Looping Through a String -- Since strings are arrays, we can loop through the characters in a string, with a for loop.

for x in "banana":
    print(x)

# String Length -- To get the length of a string, use the len() function
print("length of b variable")
print(len(b))

# Check String -- To check if a certain phrase or character is present in a string, we can use the keyword in. 

txt = "The best things in life are free!"

print("free" in txt)

# using it in an if statement:

# print only if "free" is present

if "free" in txt:
    print("Yes, 'free' is present")
# else:
#     print("not in the txt")

# Check if NOT -- To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

# check if "expensive" is not present in the following text:
print("expensive" not in txt)
print("things" not in txt) #it return false because it's in the txt

#using it in an if statement

if "expensive" not in txt:
    print("NO, 'expensive' is not present!")