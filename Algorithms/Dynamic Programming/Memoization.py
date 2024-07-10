import time, random

times = []


def square_no_memo(num):
    return num**2


array = [random.randint(1, 10) for _ in range(10000000)]
t1 = time.time()
for i in range(len(array)):
    print(square_no_memo(array[i]))
t2 = time.time()
times.append(t2 - t1)
