word = input("Please enter a value ")
vowels = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü']
total = 0

for i in vowels:
    total += word.count(i)

print(f"{word} has {total} vowels")
