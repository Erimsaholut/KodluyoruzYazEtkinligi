import math

num = int(input("Please Enter Value\n"))
sqrNum = int(math.sqrt(num)) + 1

for i in range(2, sqrNum):
    if (num % i == 0):
        print("Not Prime")
        break
    elif (i == sqrNum - 1):
        print("Prime")
