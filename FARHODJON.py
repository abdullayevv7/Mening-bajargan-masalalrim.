##1-masala
# boshlangich_summasi = float(input("Boshlang'ich summani kiriting: "))
# foiz = 5
# maqsad_summasi = 2 * boshlangich_summasi
# joriy_summasi = boshlangich_summasi
# yillar = 0
#
# while joriy_summasi < maqsad_summasi:
#     joriy_summasi = joriy_summasi * (1 + foiz / 100)
#     yillar += 1
#
# print(f"Pul ikki baravar bo'lishi uchun {yillar} yil kerak bo'ladi.")


##2-masala
# boshlangich_bakteriya_soni = 1
# maqsad = 1_000_000
# kopayish_vaqti = 0
#
# while boshlangich_bakteriya_soni < maqsad:
#     boshlangich_bakteriya_soni *= 2
#     kopayish_vaqti += 20
#
# soat = kopayish_vaqti // 60
# daqiqa = kopayish_vaqti % 60
#
# print(f"Natijaga erishish uchun ketgan vaqt: {soat} soat va {daqiqa} daqiqa")


##3-masala
# qarz = float(input("Qarz summasini kiriting (so'mda): "))
#
# foiz = float(input("Oylik foiz stavkasini kiriting (%): "))
#
# tolov = float(input("Har oy to'laydigan summani kiriting (so'mda): "))
#
# minimal_tolov = qarz * (foiz / 100)
# if tolov <= minimal_tolov:
#     print("Siz har oy qarzga qo‘shilayotgan foizdan kam to‘lamoqdasiz.")
#     print("Qarz hech qachon tugamaydi! To‘lov miqdorini oshiring.")
# else:
#     oylar = 0
#
#     while qarz > 0:
#         qarz += qarz * (foiz / 100)
#         qarz -= tolov
#         oylar += 1
#
#     print(f"Qarzdan qutulish uchun {oylar} oy kerak bo‘ladi.")


##4-masala
# 1. Boshlang'ich batareya darajasi (foizda)
# batareya = 100
#
# # 2. Har soatda yo'qotiladigan foiz (15%)
# yoqotish_foizi = 15
#
# # 3. Minimal daraja (telefon o'chadigan chegara)
# minimal = 20
#
# # 4. Soat hisoblagichi
# soat = 0
#
# # 5. Batareya 20% dan pastga tushmaguncha ishlayveradi
# while batareya > minimal:
#     # 6. Har soat batareya joriy qiymatining 15% ga kamayadi
#     batareya = batareya * (1 - yoqotish_foizi / 100)
#
#     # 7. Soatni oshiramiz
#     soat += 1
#
#     # 8. Har soat holatini ko'rsatamiz (ixtiyoriy)
#     print(f"{soat}-soat: Batareya {batareya:.2f}%")
#
# # 9. Natija
# print(f"\n📱 Telefon {soat} soatdan so'ng o'chadi (batareya {minimal}% dan past).")


##5-masala
# boshlangich_mahsulot_miqdori = int(input("Mahsulot miqdorini kiriting: "))
# kunlik_sotish_miqdori = int(input("Kunlik sotish miqdorini kiriting: "))
# kunlik_kelish_miqdori = int(input("kunlik kelish miqdorni kiriting: "))
# mahsulot_miqdori = boshlangich_mahsulot_miqdori
# day = 0
#
# while mahsulot_miqdori > 0:
#     mahsulot_miqdori+=kunlik_kelish_miqdori
#     mahsulot_miqdori-=kunlik_sotish_miqdori
#     day+=1
#
# print(f"{day}-kun oxirida qoldiq: {mahsulot_miqdori} dona.")


##6-masala
# idish_hajmi = 2000
# suv = 0
# daqiqa = 0
#
# while suv < idish_hajmi:
#     suv += 200 - 50
#     daqiqa += 1
#
# print(f"Idish {daqiqa} daqiqada to'ladi.")


##7-masala
# yoqilgi = 60
# sarf = 8
# masofa = 0
#
# while yoqilgi >= sarf / 10:
#     yoqilgi -= sarf / 10
#     masofa += 10
#
# print(f"Avtomobil {masofa} km masofani bosib o‘tadi.")


##8-masala
# populyatsiya = 100000
# foiz = 0.03
# maqsad = 200000
# yil = 0
#
# while populyatsiya < maqsad:
#     populyatsiya += populyatsiya * foiz
#     yil += 1
#
# print(f"{yil} yildan keyin populyatsiya {int(populyatsiya)} ga yetadi.")


##9-masala
# general_tarffic = int(input("Enter your internet traffic: "))
# amount_of_consumption = int(input("Set daily intake amount: "))
# traffic = general_tarffic
# day = 0
#
# while traffic > 0:
#     traffic -= amount_of_consumption
#     day+=1
#     if traffic < 0:
#         traffic = 0
#     foiz = (traffic / general_tarffic) * 100
#     print(f"{day}-kun: {traffic:.2f}GB qoldi! ({foiz:.1f}%)")
#
#
#     if foiz <= 20 and foiz > 10:
#         print("Trafik kam qoldi!")
#     elif foiz <= 10 and traffic > 0:
#         print("Trafik juda kam!")
#
# print(f"Trafik {day} kundan keyin tugaydi!")


##10-masala
# baholar = [4, 4, 5, 4]
# maqsad = 4.5
# yangi_baho = 5
# qadamlar = 0
#
# while sum(baholar) / len(baholar) < maqsad:
#     baholar.append(yangi_baho)
#     qadamlar += 1
#
# print(f"{qadamlar} ta {yangi_baho} baho kerak bo'ladi.")


##11-masala
# buyurtmalar_soni = 20
# tayyorlash_vaqti = 5
# vaqt = 0
#
# while buyurtmalar_soni > 0:
#     buyurtmalar_soni -= 1
#     vaqt += tayyorlash_vaqti
#
# print(f"Navbatdagi barcha buyurtmalar uchun {vaqt} daqiqa kutish kerak.")


##12-masala
# kredit_summasi = 300_000_000
# oylik_tolov = 15_000_000
# month = 0
#
# while kredit_summasi > 0:
#     kredit_summasi-=oylik_tolov
#     month+=1
# print(f"Kreditni to'lash uchun {month} oy kerak!")


##13-masala
# n = int(input("Boshlang'ich sonni kiriting: "))
# qadam = 0
#
# while n != 1:
#     if n % 2 == 0:
#         n = n // 2
#     else:
#         n = 3 * n + 1
#     qadam += 1
#     print(n)
#
# print(f"1 ga yetish uchun {qadam} ta qadam kerak bo‘ladi.")


##14-masala
# def kaprekar(n):
#     qadam = 0
#     while n != 6174:
#         s = str(n).zfill(4)
#         katta = int("".join(sorted(s, reverse=True)))
#         kichik = int("".join(sorted(s)))
#         n = katta - kichik
#         qadam += 1
#     return qadam
#
# print(kaprekar(3524))


##15-masala
# def paskal(n):
#     uchburchak = [[1]]
#     for i in range(1, n):
#         oldingi = uchburchak[-1]
#         yangi = [1]
#         for j in range(1, len(oldingi)):
#             yangi.append(oldingi[j-1] + oldingi[j])
#         yangi.append(1)
#         uchburchak.append(yangi)
#     return uchburchak
#
# for qator in paskal(5):
#     print(qator)


##16-masala
# def sehrli_kvadrat(n):
#     if n % 2 == 0:
#         return "Faqat toq sonlar uchun!"
#
#     kvadrat = []
#     i = 0
#     while i < n:
#         qator = []
#         j = 0
#         while j < n:
#             qator.append(0)
#             j += 1
#         kvadrat.append(qator)
#         i += 1
#
#     qator = 0
#     ustun = n // 2
#
#     son = 1
#     while son <= n * n:
#         kvadrat[qator][ustun] = son
#
#         yangi_qator = (qator - 1) % n
#         yangi_ustun = (ustun + 1) % n
#
#         if kvadrat[yangi_qator][yangi_ustun] != 0:
#             qator = (qator + 1) % n
#         else:
#             qator = yangi_qator
#             ustun = yangi_ustun
#         son += 1
#
#     return kvadrat
#
#
# kvadrat = sehrli_kvadrat(5)
#
# if isinstance(kvadrat, list):
#     i = 0
#     while i < len(kvadrat):
#         print(kvadrat[i])
#         i += 1
#
# else:
#     print(kvadrat)


##17-masala
# def hanoy(n, A, B, C):
#     if n == 1:
#         print(f"{A} dan {C} ga ko‘chir")
#     else:
#         hanoy(n-1, A, C, B)
#         print(f"{A} dan {C} ga ko‘chir")
#         hanoy(n-1, B, A, C)
#
# hanoy(3, "A", "B", "C")


##18-masala
# def fibonacci_spiral(n):
#     if n <= 0:
#         return []
#
#     fib = [1, 1]
#     i = 2
#     while i < n:
#         fib.append(fib[i-1] + fib[i-2])
#         i += 1
#
#     koordinatalar = []
#     x, y = 0, 0
#     yunalish = 0
#
#     i = 0
#     while i < n:
#         koordinatalar.append((x, y, fib[i]))
#
#         if yunalish == 0:
#             x += fib[i]
#         elif yunalish == 1:
#             y -= fib[i]
#         elif yunalish == 2:
#             x -= fib[i]
#         else:
#             y += fib[i]
#
#         yunalish = (yunalish + 1) % 4
#         i += 1
#
#     return koordinatalar
#
# spiral = fibonacci_spiral(6)
# i = 0
# while i < len(spiral):
#     x, y, olcham = spiral[i]
#     print(f"Kvadrat {i+1}: ({x}, {y}), o'lcham: {olcham}")
#     i += 1


##19-masala
# def josephus(n, k):
#     people = list(range(1, n + 1))
#     idx = 0
#     while len(people) > 1:
#         idx = (idx + k - 1) % len(people)
#         people.pop(idx)
#     return people[0]


##20-masala
# def is_valid_sudoku(board):
#     def valid(block):
#         nums = [n for n in block if n != 0]
#         return len(nums) == len(set(nums))
#
#     for row in board:
#         if not valid(row): return False
#
#     for col in zip(*board):
#         if not valid(col): return False
#
#     for i in (0, 3, 6):
#         for j in (0, 3, 6):
#             square = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
#             if not valid(square): return False
#
#     return True


##21-masala
# def koch(n, length):
#     if n == 0:
#         return "—" * length
#     part = koch(n-1, length//3)
#     return part + "/" + part + "\\" + part


##22-masala
# def dfs(labirint, x, y, visited):
#     if labirint[x][y] == 'E': return True
#     visited.add((x, y))
#     for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
#         nx, ny = x+dx, y+dy
#         if (0 <= nx < len(labirint) and 0 <= ny < len(labirint[0]) and
#             labirint[nx][ny] != '#' and (nx, ny) not in visited):
#             if dfs(labirint, nx, ny, visited): return True
#     return False


##23-masala
# def top_dna_repeat(s):
#     longest = ""
#     for i in range(len(s)):
#         for j in range(i+1, len(s)):
#             sub = s[i:j]
#             if s.count(sub) > 1 and len(sub) > len(longest):
#                 longest = sub
#     return longest


##24-masala
# def eng_uzun_progressiya(notlar):
#     max_len = 1
#     current_len = 1
#     for i in range(2, len(notlar)):
#         if notlar[i] - notlar[i-1] == notlar[i-1] - notlar[i-2]:
#             current_len += 1
#             max_len = max(max_len, current_len)
#         else:
#             current_len = 2
#     return max_len


##25-masala
# def guess_number():
#     low, high = 1, 100
#     while True:
#         mid = (low + high) // 2
#         javob = input(f"Bu {mid} mi? (kattaroq/kichik/to‘g‘ri): ").lower()
#         if javob == "to‘g‘ri":
#             print("Topildi!")
#             break
#         elif javob == "kattaroq":
#             low = mid + 1
#         elif javob == "kichik":
#             high = mid - 1