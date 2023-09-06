import random

myList = [random.randint(1, 100) for _ in range(20)]

print(myList)

print(max(myList), min(myList))

max, min = myList[0], myList[0]

for i in myList:
    if i > max:
        max = i
    if i < min:
        min = i

print(max, min)
