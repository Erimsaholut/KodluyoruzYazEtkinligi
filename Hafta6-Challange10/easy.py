import random

myList = [random.randint(1, 100) for _ in range(20)]

print(myList)

print(max(myList))

biggest = myList[0]
for i in myList:
    if i > biggest:
        biggest = i

print(biggest)