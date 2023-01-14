# Global Variables - Create a variable outside of a function, and use it inside the function

x = "Awsome"  # variable outside function


def myfunc():
    # calling the variables or using it inside the function
    print("Python is "+x)


myfunc()

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.


def myFunction():
    x = "fantastic"
    print("Python is "+x)


myFunction()

print("Python is "+x)


# anyway if we want to use the value inside the function and outside the function . we have to use global keyword , so it will belongs to the global scope:

def globalkeyword():
    global x
    x = "Global Keyword"

globalkeyword()

print("We are using a "+x)


# also we can change the value of a global variable inside a function , refer to the variable by using the global keyword .. example in the blew;

b = "breakpint"

def changingValues():
    global b
    b = "Changing value"

changingValues()

print(b)