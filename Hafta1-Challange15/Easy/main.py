import datetime


def ask_birthdate():
    while True:
        try:
            year = int(input("Lütfen doğum yılınızı giriniz:"))
            month = int(input("Lütfen kaçıncı ayda doğduğunuzu giriniz:"))
            day = int(input("Lütfen doğduğunuz günü giriniz:"))
            birthday = datetime.datetime(year=year, month=month, day=day)
            if 1900 < year < datetime.datetime.now().year and 1 <= month <= 12 and 1 <= day <= 31:
                return birthday
            else:
                print("Hatalı değer girdiniz lütfen tekrar deneyiniz.")
        except ValueError:
            print("Geçersiz değer girdiniz. Lütfen tekrar deneyiniz.")


birthday = ask_birthdate()
currentTime = datetime.datetime.now()
age = (currentTime - birthday).days // 365
print("Yaşınız:", age)
