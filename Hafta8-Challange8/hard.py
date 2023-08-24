num = str(input("Please enter a value "))
total = 0

for i in num:
    total += int(i) ** 3


if total == int(num):
    print(f"{num} is a armstrong number !")
else:
    print(f"{num} isn't a armstrong number !")