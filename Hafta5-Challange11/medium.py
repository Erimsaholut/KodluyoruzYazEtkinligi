import random

rlist = [random.randint(1, 100) for _ in range(10)]

print(rlist)
print(sum(rlist) / len(rlist))
