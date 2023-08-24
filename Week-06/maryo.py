height = -1

while height > 8 or height <= 0:
    try:
        height = int(input("Please enter height: "))
    except ValueError as err:
        pass

for i in range(height):
    for j in range(1, height - i):
        print(end=' ')

    for j in range(i + 1):
        print("#", end='')

    print(end="\t")

    for j in range(i + 1):
        print("#", end='')
    print()
