
# # Task No1 (BMİ Hesablayıcı ):

# height = float(input("Boyun: "))
# weight = float(input("Çəkin: "))

# AWH = weight / height ** 2

# if AWH < 18.5:
#     print("Arıqsan.")
# elif AWH < 24.9:
#     print("Normal.")
# elif AWH <= 29.9:
#     print("Artıq çəki.")
# else:
#     print("Obez.")

# # Task No2 (Üçbucaq Növü):

# import sys

# sys.stdout.write("Tərəf 1:")
# sys.stdout.flush()
# a = int(sys.stdin.readline())

# sys.stdout.write("Tərəf 2:")
# sys.stdout.flush()
# b = int(sys.stdin.readline())

# sys.stdout.write("Tərəf 3:")
# sys.stdout.flush()
# c = int(sys.stdin.readline())

# if a + b > c and a + c > b and b + c > a:
#     print("Mövcuddur", end=" ")
#     if a == b == c:
#         print("Bərabərtərəfli")
#     else:
#         if a == b or b == c or a == c:
#             print("Bərabəryanlı")
#         else:
#             print("Müxtəliftərəfli")
# else:
#     print("Mövcud deyil")

# # Task No3 (İl Növü):

# import sys
# sys.stdout.write("İl daxil et:")
# sys.stdout.flush()
# year = int(sys.stdin.readline())

# if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
#     print(f"{year} uzun ildir.")
# else:
#     print(f"{year} uzun il deyil.")

# # Task No4 (Qiymət Sistemi):

# subjectScoreArray = [85, 90, 75, 92, 88]

# average = sum(subjectScoreArray) / len(subjectScoreArray) 

# if average >= 90:
#     print("Fərqlənmə.")
# elif average >= 80:
#     print("Yaxşı.")
# elif average >= 70:
#     print("Kafi.")
# elif average >= 60:
#     print("Zəif.")
# else:
#     print("Dərsi təkrarlayacaq")

# # Task No5 (Taksi Tarifi):

# mesafe, vaxt = input("Məsafə (km) və vaxt (gecə/gündüz) daxil edin:").split()
# mesafe = float(mesafe)
# vaxt = str(vaxt)
# minimumOdenis = 2

# tamOdenis = minimumOdenis + max(0, mesafe - 3) * 0.80

# if vaxt == "gecə":
#     tamOdenis *= 1.5

# print(f"Qiymət: {tamOdenis:.2f} AZN")

# # Task No6 (Tərəzinin Balansı):

# deyer1, deyer2 = input("Hər iki cəftin kütləsini daxil edin (kq): ").split()
# deyer1 = float(deyer1)
# deyer2 = float(deyer2)
# mutleqDeyer = abs(deyer1 - deyer2)

# if deyer1 == deyer2:
#     print("Balans var.")
# else:
#     print(f"Balans yoxdur, fərq: {mutleqDeyer} kq")

# # Task No7 (Elektrik Hesabı):

# istehlak = float(input("İstehlakı daxil et (kWt): "))

# if istehlak <= 100:
#     mebleg = istehlak * 0.06
# elif istehlak <= 300:
#     mebleg = 100 * 0.06 + (istehlak - 100) * 0.10
# else:
#     mebleg = 100 * 0.06 + 200 * 0.10 + (istehlak - 300) * 0.14

# print(f"Cəm məbləğ: {mebleg} AZN")


# # +===================================================================
# # +===================================================================
# # +===================================================================

# # Star triangle:

# value = int(input("Dəyər daxil et:"))
# for r in range(1, value + 1):
#     for space in range(value - r):
#         print(" ", end="")
    
#     for star in range(2 * r - 1):
#         print("*", end="")
#     print()

# # Calculator:

# try:
#     value1 = int(input("Dəyər daxil et: "))
#     operator = input("Operator daxil edin (+ - * / % **): ")
#     value2 = int(input("Dəyər daxil et: "))
#     if operator == "+":
#         print(f"Cavab: {value1 + value2}")
#     elif operator == "-":
#         print(f"Cavab: {value1 - value2}")
#     elif operator == "*":
#         print(f"Cavab: {value1 * value2}")
#     elif operator == "/":
#         print(f"Cavab: {value1 / value2}")
#     elif operator == "%":
#         print(f"Cavab: {value1 % value2}")
#     elif operator == "**":
#         print(f"Cavab: {value1 ** value2}")
#     else:
#         print("Şərt ödənilmədi!")
# except Exception as e:
#     print(f"Xəta: {e}")
# print("=====================================")

# # +===================================================================
# # +===================================================================
# # +===================================================================

# Sadə ədədlərin tapılması:
# numeral = int(input("Dəyər daxil et: "))
# simpleNumbers = []

# for i in range(2, numeral):
#     chachNumber = 0 
#     for x in range(2, i):
#         if i % x == 0:
#             chachNumber += 1
#     if chachNumber == 0:
#         simpleNumbers.append(i)
# print(simpleNumbers)

# # +===================================================================
# # 05.09.2026

# # 1.  Zər Simulyatoru
# # random.randint() istifadə edərək iki zəri eyni anda atın. Hər zərin dəyərini ayrıca çap edin. 
# #Əgər hər iki zər eyni ədədi göstərirsə ekranda 'Dublet!' yazısını göstərin.
# import random

# rollOne = random.randint(1, 6)
# rollTwo = random.randint(1, 6)

# if rollOne == rollTwo:
#     print(f"Rol One {rollOne}, Rol Twk {rollTwo}, \n \t Dublet!")
# else:
#     print(f"Rol One {rollOne}, Rol Twk {rollTwo}, \n \t Not Dublet!")

# # +===================================================================

# # 2. Təsadüfi Koordinat Generatoru
# # Robot 10×10 ölçülü bir meydançada hərəkət edir. random.randint() ilə robotun x və y koordinatlarını generasiya edin. 
# # Koordinatları 'Robot mövqeyi: (x, y)' formatında çap edin. Bunu 5 dəfə təkrarlayın və hansı sətirlərdə eyni koordinatın çıxdığını yoxlayın.

# import random

# countAxisX = list()
# countAxisY = list()

# for i in range(5):
#     axisX = random.randint(1, 10)
#     axisY = random.randint(1, 10)
#     print(f"{i + 1}. Robot mövqeyi: ({axisX}, {axisY})")
#     countAxisX.append(axisX)
#     countAxisY.append(axisY)
# print(f"Axis X: {countAxisX}, \nAxis Y: {countAxisY}")

# # +===================================================================

# 3. Təsadüfi Rəng Seçici
# ['qırmızı', 'mavi', 'yaşıl', 'sarı', 'narıncı', 'bənövşəyi'] siyahısından random.choice() ilə bir rəng seçin. 
# Seçilən rəngi 'Robota verilən rəng: [rəng]' formatında çap edin. Proqramı for dövrəsi ilə 5 dəfə işlədin.

# import random
# colors = ['qırmızı', 'mavi', 'yaşıl', 'sarı', 'narıncı', 'bənövşəyi', 'qara', 'ağ']

# for i in range(5):
#     print(f"{i + 1}. {random.choice(colors)}")

# # +===================================================================

# # 6. Cüt Ədəd Generatoru
# # random.randrange() istifadə edərək 2-100 arasından 6 cüt ədəd generasiya edin. Hər ədədi siyahıya əlavə edin. Siyahını çap edin. Siyahının cəmini tapın.

# import random

# evenNumbers = list()

# for x in range(6):
#     evenNumber  = random.randrange(0, 100, 2)
#     evenNumbers.append(evenNumber)

# print(f"List: {evenNumbers}, \nSum: {sum(evenNumbers)}")

# # +===================================================================

## 7. Siyahı Qarışdırıcı
## 1-dən 10-a qədər ədədlərdən ibarət siyahı yaradın. random.shuffle() ilə qarışdırın. Qarışmış siyahını çap edin. Siyahının ilk üç elementini ekranda göstərin.

# import random

# numList = list()

# for ziyaya_inad_bele_ad_verirem_ziya_partda in range(1, 11):
#     numbers = ziyaya_inad_bele_ad_verirem_ziya_partda
#     numList.append(numbers)

# print(f"Siyahı: {numList}")

# random.shuffle(numList)

# print(f"Qarışmış siyahı: {numList}")

# print(f"İlk üç element: {numList[:3]}")

# # +===================================================================

