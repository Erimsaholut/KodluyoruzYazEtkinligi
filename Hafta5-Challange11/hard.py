import random
rlist = [random.randint(1, 100) for _ in range(100)]

rlist.sort()

x = int(input("Please enter a value "))

print(f"{x} number repeated {rlist.count(x)} times")
