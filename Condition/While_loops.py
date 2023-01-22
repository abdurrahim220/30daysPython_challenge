i = 1
while i < 6:
    print(i)
    i += 1

# The break Statement -- with the break statement we can stop the loop even if the while condition is true!

i = 1
while i < 6 :
    print(i)
    if i == 3:
        break
    i += 1

while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
else:
   print("i is no longer less than 6")