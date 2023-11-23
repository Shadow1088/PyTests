def func(array):
    z = 0
    list1 = []
    for i in array:
        if i != 0:
            list1.append(i)
        else:
            z += 1
    list1.extend([0] * z)
    return list1

import time
import random

n = 100000
list0 = [random.randint(0, 9) for _ in range(n)]
start = time.time()
func(list0)
end = time.time()
print(f"Time taken: {end - start}")
print(len(func(list0)))



    