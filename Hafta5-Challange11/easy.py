def facto(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return x * facto(x - 1)


num = int(input("Please enter a number for factorial calculation"))
print(facto(num))
