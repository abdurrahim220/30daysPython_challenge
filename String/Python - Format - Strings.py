# String Format -- The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:

age = 36
txt = "My name is John , and I am {}"

print(txt.format(age))


# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

qu_n = 3
it_d = 567
price = 49.95

myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(qu_n,it_d,price))
# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
myorder2= "I want {2} pieces of item {0} for {1} dollars."
print(myorder2.format(qu_n,it_d,price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

