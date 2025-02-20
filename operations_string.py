s1 = "hello"
s2 = "world"
print(s1 + " " + s2)
print(s1, "hello")
print(3*s2)
print((10//2)*s1)
# len function gives you the size of the string
print(s1, len(s1))
print(3*s2, len(3*s2))
for c in s2:
    print(c*4, end="")
print()

new_string = ""
for c in s2:
    new_string += c*4 # same as: new_string = new_string + 4 * c
print(new_string)

# in can be used to check if one stirng is inside another
print("h" in s1) # true
print("d" in s2) # true
print("x" in s1) # false
print("wor" in s2) # true
