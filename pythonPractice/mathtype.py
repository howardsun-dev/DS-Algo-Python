import math

# Division is decimal by default
print(5 / 2)

# Integer division, rounds down, not toward zero
print(5 // 2)

print(-3 // 2)
print((int(-3 / 2)))

# Modulo similar
print(10 % 3)

# Except for negative values
print(-10 % 3)

print(math.fmod(-10, 3))


print(math.floor(3 / 2))
print(math.ceil(3 / 2))
print(math.sqrt(2))
print(math.pow(2, 3))

# Max / Min Int
float("inf")
float("-inf")

# Python numbesr are infinite so they never overflow
print(math.pow(2, 200))
