'''
Escape Character
To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

'''

txt = "My name is \"Md Abdur Rahim\" form Rajshahi"

print(txt)


# single quote

s_q = "It\'s alright"
print(s_q)

b_s = "This will insert \\ (backlash)"
print(b_s)

# new line

n_l = "New\nLine"
print(n_l)

# charriage Return 

c_r = "123654r\rReturn!"
print(c_r)

# tab
print("\tHello".expandtabs(tabsize=8))

# backspace

txt = "Hello\bWorld"

print(txt)