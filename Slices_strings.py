s = "abcdefghijklmnop"
print(s)
print(s[1:4], s[6:9])
print(s[:4], s[6:])
print(s[1:10:2])
print(s[::-1])
print("racecar"[::-1])

# this is how you "replace" a letter
s= "cat"
s = "r" + s[1:]
print(s)

s = "seven" # i want to change it to se7en
s = s[:2] + "7" + s[3:]
print(s)
