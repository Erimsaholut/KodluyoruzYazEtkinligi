import random

myList = [random.randint(1, 100) for _ in range(20)]
total = 0

for i in myList:
    if i % 2 == 0:
        total += i

print(myList)
print(total)
