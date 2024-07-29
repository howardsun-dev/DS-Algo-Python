# Arrays (called lists in python)
arr = [1, 2, 3]
print(arr)


# Can be used as stacks
arr.append(4)
arr.append(5)
print(arr)

arr.pop()
print(arr)

arr.insert(1, 7)
print(arr)

arr[0] = 0
arr[3] = 3
print(arr)


# Init arr of size n with default value of 1
n = 5
arr = [1] * 5

print(arr)
print(len(arr))
print(arr[-1])  # Read last value

# Sublist (aka slicing)

print(arr[1:3])


# Unpacking
a, b, c = [1, 2, 3]
print(a, b, c)


# loop through array
nums = [1, 2, 3]

# using index
for i in range(len(nums)):
    print(nums[i])

# without index
for n in nums:
    print(n)

# WIth index and value
for i, n in enumerate(nums):
    print(i, n)

# loop through multiple arrays simultaneously with unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)


# reversing array
nums = [1, 2, 3]
nums.reverse()
print(nums)
