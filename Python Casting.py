'''
There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

    --int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)

    --float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)

    --str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

'''
# int time
x = int(1) # it will be 1 
x = int(2.89) # it will be 2
x = int ("3") # it will be 3

#float time
x = float ("3") # it will be 3.0
x = float(1) # it will be 1.0
x = float(2.89) # it will be 2.89

# String time

x = str("s1") # it will be s1 
x = str("2.89") # it will be 2.89

