import time


def fibonacci(n):
    if n < 2:
        return n
    else:
        return (n - 1) + (n - 2)


cache = {}


def dynamic_fib(n):
    if n in cache:
        return cache[n]
    else:
        if n < 2:
            return n
        else:
            cache[n] = (n - 1) + (n - 2)
            return cache[n]


# Test Time Difference

t1 = time.time()
print(fibonacci(55))
t2 = time.time()
print(t2 - t1)

t1 = time.time()
print(dynamic_fib(55))
t2 = time.time()
print(t2 - t1)
