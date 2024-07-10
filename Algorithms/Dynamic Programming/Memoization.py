import time, random
from functools import lru_cache

times = []


def square_no_memo(num):
    return num**2


array = [random.randint(1, 10) for _ in range(10000000)]
t1 = time.time()
for i in range(len(array)):
    print(square_no_memo(array[i]))
t2 = time.time()
times.append(t2 - t1)

cache = {}


def square_with_memo(num):
    if num in cache:
        return cache[num]
    else:
        cache[num] = num**2
        return cache[num]


t1 = time.time()
for i in range(len(array)):
    print(square_with_memo(array[i]))
t2 = time.time()
times.append(t2 - t1)


@lru_cache(maxsize=10000)
def squaring(number):
    return number**2


print(array)
t1 = time.time()
for i in range(len(array)):
    print(squaring(array[i]))
t2 = time.time()
times.append(t2 - t1)

print(times)
print(cache)


# print(squaring.cache_info())
