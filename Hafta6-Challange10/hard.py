x = float(input("Enter a value "))
y = int((x / 2) + 1)
sum = 0

for i in range(1, y):
    if x % i == 0:
        sum += i
        print(i)
print(f"sum:{sum}")
