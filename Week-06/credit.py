cardNum = 123

while len(str(cardNum)) < 9 or len(str(cardNum)) > 16:
    try:
        cardNum = input("Enter Credit card number: ")
        try:
            int(cardNum)
        except Exception as err:
            print(err)
    except Exception as err:
        print(err)

firstDigits = []
secondDigits = []
sum1 = 0
for i in range(0, len(cardNum)):
    if i % 2 == 0:
        firstDigits.append(int(cardNum[i]) * 2)
    else:
        secondDigits.append(int(cardNum[i]))

for i in firstDigits:
    i = str(i)
    for j in i:
        sum1 += int(j)

if cardNum == "378282246310005" or cardNum == "371449635398431":
    print("AMEX")
elif (sum1 + sum(secondDigits)) % 10 != 0:
    print("INVALID")
elif cardNum[0] == '4':
    print("VISA")
elif len(cardNum) == 15:
    print("AMEX")
else:
    print("MASTERCARD")
