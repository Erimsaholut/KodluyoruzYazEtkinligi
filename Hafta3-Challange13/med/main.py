# easy way
# my_word = input("Please enter a word: \n")
# print(my_word.upper())


# Hard way

my_word = input("Please enter a word: \n")
key = ord("A") - ord("a")
converted_word = ""

for i in my_word:
    if ord(i) >= 97:
        converted_word += chr(ord(i) + key)
    else:
        converted_word += i

print(converted_word)
