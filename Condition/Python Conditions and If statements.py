a = 33
b = 33

if a>b :
    print("a is greater than b")
elif a == b:
    print("both are equal!")
else:
    print("b is greater than a")


# short hand if

c = 28
d = 25

if c > d : print("b is grater than a")

# Short Hand If ... Else
a = 2
b = 5

print("A") if a>b else print("B")

a = 3302
b = 330
print("A") if a>b else print("==") if a == b else print("b")

# And -- and keyword is a logical operator , and is used to combine conditional statements: it will only work when is both condition is true!!

a = 200
b = 33
c = 500

if a > b and c > a:
    print("Both conditions are True")
else: 
    print("Not Truth")

# or keyword is a logical operator -- and is used to combine conditional statement .. it will work when is condition is true!!

if a > b or a > c:
    print("At least one of the two conditions is True!")

# Nested if 

x = 15 
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!!")
    else:
        print("But not above 20.!")