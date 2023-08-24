import sys

if len(sys.argv) != 2:
    print("Usage: python caesar.py k")
    sys.exit(1)

k = int(sys.argv[1])

plaintext = input("plaintext: ")

ciphertext = ""

for char in plaintext:
    if char.isalpha():
        if char.isupper():
            shifted = chr(((ord(char) - ord('A') + k) % 26) + ord('A'))
        else:
            shifted = chr(((ord(char) - ord('a') + k) % 26) + ord('a'))
        ciphertext += shifted
    else:
        ciphertext += char

print("ciphertext:", ciphertext)
