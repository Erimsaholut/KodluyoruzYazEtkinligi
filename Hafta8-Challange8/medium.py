dizi = [3, 5, 87, 234, 756, 97, 223, 657, -32, -3, 14]

for i in range(0, len(dizi)):
    for j in range(0, len(dizi) - 1):
        if dizi[j] > dizi[j + 1]:
            dizi[j], dizi[j + 1] = dizi[j + 1], dizi[j]

print(dizi)
if len(dizi) % 2 != 0:
    print(dizi[round(len(dizi) / 2) - 1])
else:
    print((dizi[round(len(dizi) / 2) - 1]+dizi[round(len(dizi) / 2)])/2)


