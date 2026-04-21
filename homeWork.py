# Task No1 (BMİ Hesablayıcı ):

height = float(input("Boyun: "))
weight = float(input("Çəkin: "))

AWH = weight / height ** 2

if AWH < 18.5:
    print("Arıqsan.")
elif AWH < 24.9:
    print("Normal.")
elif AWH <= 29.9:
    print("Artıq çəki.")
else:
    print("Obez.")

# Task No2 (Üçbucaq Növü):

import sys

sys.stdout.write("Tərəf 1:")
sys.stdout.flush()
a = int(sys.stdin.readline())

sys.stdout.write("Tərəf 2:")
sys.stdout.flush()
b = int(sys.stdin.readline())

sys.stdout.write("Tərəf 3:")
sys.stdout.flush()
c = int(sys.stdin.readline())

if a + b > c and a + c > b and b + c > a:
    print("Mövcuddur", end=" ")
    if a == b == c:
        print("Bərabərtərəfli")
    else:
        if a == b or b == c or a == c:
            print("Bərabəryanlı")
        else:
            print("Müxtəliftərəfli")
else:
    print("Mövcud deyil")

# Task No3 (İl Növü):

import sys
sys.stdout.write("İl daxil et:")
sys.stdout.flush()
year = int(sys.stdin.readline())

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print(f"{year} uzun ildir.")
else:
    print(f"{year} uzun il deyil.")

# Task No4 (Qiymət Sistemi):

subjectScoreArray = [85, 90, 75, 92, 88]

average = sum(subjectScoreArray) / len(subjectScoreArray) 

if average >= 90:
    print("Fərqlənmə.")
elif average >= 80:
    print("Yaxşı.")
elif average >= 70:
    print("Kafi.")
elif average >= 60:
    print("Zəif.")
else:
    print("Dərsi təkrarlayacaq")

# Task No5 (Taksi Tarifi):

mesafe, vaxt = input("Məsafə (km) və vaxt (gecə/gündüz) daxil edin:").split()
mesafe = float(mesafe)
vaxt = str(vaxt)
minimumOdenis = 2

tamOdenis = minimumOdenis + max(0, mesafe - 3) * 0.80

if vaxt == "gecə":
    tamOdenis *= 1.5

print(f"Qiymət: {tamOdenis:.2f} AZN")

# Task No6 (Tərəzinin Balansı):

deyer1, deyer2 = input("Hər iki cəftin kütləsini daxil edin (kq): ").split()
deyer1 = float(deyer1)
deyer2 = float(deyer2)
mutleqDeyer = abs(deyer1 - deyer2)

if deyer1 == deyer2:
    print("Balans var.")
else:
    print(f"Balans yoxdur, fərq: {mutleqDeyer} kq")

# Task No7 (Elektrik Hesabı):

istehlak = float(input("İstehlakı daxil et (kWt): "))

if istehlak <= 100:
    mebleg = istehlak * 0.06
elif istehlak <= 300:
    mebleg = 100 * 0.06 + (istehlak - 100) * 0.10
else:
    mebleg = 100 * 0.06 + 200 * 0.10 + (istehlak - 300) * 0.14

print(f"Cəm məbləğ: {mebleg} AZN")
