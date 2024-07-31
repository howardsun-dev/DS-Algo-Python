# Sorting array
arr = [5, 4, 7, 3, 8]
arr.sort()
print(arr)

# Sort in reverse order/descending
arr.sort(reverse=True)
print(arr)

# Defaults to alphabetical
arr = ["bob", "alice", "jane", "doe"]
arr.sort()
print(arr)

# Custom sort (by string len)
arr.sort(key=lambda x: len(x))
print(arr)

# List comprehension
arr = [i + i for i in range(5)]
print(arr)

# 2-D Lists
arr = [[0] * 4 for i in range(4)]
print(arr)
