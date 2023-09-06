meth = input("Bir metin yazınız: ")

for i in range(len(meth.split())):
    try:
        if meth.split()[i + 1] == meth.split()[i]:
            print("İkileme kullanıdınız")
            break
    except IndexError:
        print("İkileme bulunamadı.")
        pass

# meth = input("Bir metin yazınız: ")
# words = meth.split()
#
# if any(words[i] == words[i + 1] for i in range(len(words) - 1)):
#     print("İkileme kullanıldı.")
# else:
#     print("İkileme bulunamadı.")
