# Strings are similar to arrays

s = "abc"
# Sliced from index 0 to index 2, but inclusive
print(s[0:2])

# Strings are immutable, but can be updated, anytime string is modified it is O(n)
# Since it creates a new string
s += "def"
print(s)

# Valid numeric strings can be converted
print(int("123") + int("123"))

# Numbers can be converted into strings
print(str(123) + str(123))

# In case you need ASCII values of a char
print(ord("a"))
print(ord("b"))

# Combine a list of strings (with an empty string delimiter)
strings = ["ab", "cd", "ef"]
print(" ".join(strings))
