text = input("Lütfen bir metin giriniz:")
rep = [0, 'a']
for i in text:
    j = text.count(i)
    if i != " " and j > rep[0]:
        rep[0] = j
        rep[1] = i

print(f"En çok tekrar eden harf {rep[0]} kere ile {rep[1]} harfi !")
