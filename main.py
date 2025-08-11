# #26-masala
# # royxat = [10, 3, 25, 7, -2, 30]
# #
# #
# # eng_katta = royxat[0]
# # eng_kichik = royxat[0]
# #
# #
# # for son in royxat[1:]:
# #     if son > eng_katta:
# #         eng_katta = son
# #     if son < eng_kichik:
# #         eng_kichik = son
# #
# # print("Eng katta son:", eng_katta)
# # print("Eng kichik son:", eng_kichik)
#
#
# ##27-masala
# # son = 1234
# #
# #
# # son = abs(son)
# #
# # raqamlar_yigindisi = 0
# #
# #
# # for num in str(son):
# #     raqamlar_yigindisi += int(num)
# #
# # print("Raqamlar yig'indisi:", raqamlar_yigindisi)
#
#
# #28-masala
# # son = 28
# # boluvchilar_yigindisi = 0
# #
# # for i in range(1, son):
# #     if son % i == 0:
# #         boluvchilar_yigindisi += i
# #
# # if boluvchilar_yigindisi == son:
# #     print(son, "— mukammal son")
# # else:
# #     print(son, "— mukammal son emas")
#
#
# #29-masala
# # son = 153
# #
# # raqamlar = str(son)
# # daraja = len(raqamlar)
# # yigindi = 0
# #
# # for raqam in raqamlar:
# #     yigindi += int(raqam) ** daraja
# #
# # if yigindi == son:
# #     print(son, "— Armstrong son")
# # else:
# #     print(son, "— Armstrong son emas")
#
#
# # def armstrong_sonmi(n):
# #     raqamlar = [int(raqam) for raqam in str(n)]
# #     daraja = len(raqamlar)
# #     yigindi = sum(raqam ** daraja for raqam in raqamlar)
# #
# #     return yigindi == n
# #
# #
# # print(armstrong_sonmi(153))
# # print(armstrong_sonmi(370))
# # print(armstrong_sonmi(123))
#
#
# #30-masala
# matn = "Hello World, I'm back"
#
#
# sozlar = matn.split()
#
#
# sozlar_soni = {}
#
#
# for soz in sozlar:
#     if soz in sozlar_soni:
#         sozlar_soni[soz] += 1
#     else:
#         sozlar_soni[soz] = 1
#
#
# for soz, soni in sozlar_soni.items():
#     print(f"{soz}: {soni} marta")
#
#
# #31-masala
# sonlar = [90, 1, 4, 17, 7, 77, 99]
#
# n = len(sonlar)
#
# for i in range(n - 1):
#
#     for j in range(n - 1 - i):
#         if sonlar[j] > sonlar[j + 1]:
#             # Joylarini almashtirish
#             vaqtincha = sonlar[j]
#             sonlar[j] = sonlar[j + 1]
#             sonlar[j + 1] = vaqtincha
#
# print("Saralangan ro'yxat:", sonlar)
#
#
# #32-masala
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# yigindi = 0
#
# for qator in matrix:
#     for element in qator:
#         yigindi += element
#
# print("Elementlar yig'indisi:", yigindi)
#
#
# #33-masala
# royxat = [4, 2, 4, 6, 2, 4, 3, 2, 2, 4]
#
# takrorlar = {}
#
# for son in royxat:
#     if son in takrorlar:
#         takrorlar[son] += 1
#     else:
#         takrorlar[son] = 1
#
# eng_kop_son = None
# eng_kop_marta = 0
#
# for son, miqdor in takrorlar.items():
#     if miqdor > eng_kop_marta:
#         eng_kop_marta = miqdor
#         eng_kop_son = son
#
# print("Eng ko'p takrorlangan son:", eng_kop_son)
# print("Takrorlanish soni:", eng_kop_marta)
#
#
# #34-masala
# matn1 = "listen"
# matn2 = "silent"
#
# if sorted(matn1) == sorted(matn2):
#     print("Bu ikki matn anagram.")
# else:
#     print("Bu ikki matn anagram emas.")
#
#
# #35-masala
# son = input("Sonni kirit: ")
#
# teskari = int(str(son)[::-1])
#
# print("Teskari tartibdagi son:", teskari)
#
#
# #36-masala
# balandlik = 5
#
# for i in range(1, balandlik + 1):
#     # Bo'sh joylar
#     print(" " * (balandlik - i), end="")
#     # Yulduzchalar
#     print("*" * (2 * i - 1))
#
#
# #37-masala
# a = 36
# b = 60
#
# kichik = min(a, b)
# ekub = 1
#
# for i in range(1, kichik + 1):
#     if a % i == 0 and b % i == 0:
#         ekub = i
#
# print("EKUB:", ekub)
#
#
# #38-masala
# royxat = [3, 8, 12, 17, 23, 29, 35, 42]
# qidirilayotgan = 23
#
# boshi = 0
# oxiri = len(royxat) - 1
# topildi = False
#
# while boshi <= oxiri:
#     orta = (boshi + oxiri) // 2
#     if royxat[orta] == qidirilayotgan:
#         print("Element topildi. Indeksi:", orta)
#         topildi = True
#         break
#     elif qidirilayotgan > royxat[orta]:
#         boshi = orta + 1
#     else:
#         oxiri = orta - 1
#
# if not topildi:
#     print("Element ro'yxatda mavjud emas.")
#
#
# #39-masala
# N = 6
# uchburchak = []
#
# for i in range(N):
#     qator = []
#     for j in range(i + 1):
#         if j == 0 or j == i:
#             qator.append(1)
#         else:
#             qator.append(uchburchak[i-1][j-1] + uchburchak[i-1][j])
#     uchburchak.append(qator)
#     print(qator)
#
#
# #40-masala
# sonlar = [12, 15, 12, 18, 19, 15, 15, 19, 20]
#
#
# ortacha = sum(sonlar) / len(sonlar)
#
#
# sonlar_sorted = sorted(sonlar)
# n = len(sonlar)
# if n % 2 == 1:
#     mediana = sonlar_sorted[n // 2]
# else:
#     mediana = (sonlar_sorted[n // 2 - 1] + sonlar_sorted[n // 2]) / 2
#
#
# takrorlar = {}
# for son in sonlar:
#     if son in takrorlar:
#         takrorlar[son] += 1
#     else:
#         takrorlar[son] = 1
#
# moda = max(takrorlar, key=takrorlar.get)
#
#
# kvadrat_farklar = [(x - ortacha) ** 2 for x in sonlar]
# standart_ogish = (sum(kvadrat_farklar) / len(sonlar)) ** 0.5
#
# print("O'rtacha:", round(ortacha, 2))
# print("Mediana:", mediana)
# print("Moda:", moda)
# print("Standart og'ish:", round(standart_ogish, 2))