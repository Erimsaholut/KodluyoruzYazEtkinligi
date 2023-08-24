currency = [25, 10, 5, 1]
changeCounter = 0
change = -1
i = 0


while change <= 0:
    try:
        change = float(input("Change owed: ")) * 100
    except ValueError:
        pass
while change != 0:
    if currency[i] <= change:
        change -= currency[i]
        changeCounter += 1
    else:
        i += 1

print(changeCounter)
