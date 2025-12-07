# 7-m
i = int(input("Xarid summasini kirit: "))

if i < 1000000:
    print("20% chegirma")
elif i < 50000 or i >= 100000:
    print("10% chegirma")
elif i < 100000 or i < 500000:
    print("Chegirma yoq")


# 8-m
i = int(input("Soat kirit: "))

if i < 6 or i <= 12:
    print("Ertalab kofe iching")
elif i < 12 or i <= 18:
    print("Tushlik vaqti")
elif i < 18 or i <= 23:
    print("Dam olish")
elif i < 23 or i <= 6:
    print("Uxlah vaqti")


# 9-m
i = int(input("Batareya foizini kiriting (0-100): "))

if i > 80:
    print("Batareya yaxshi holatda!")
elif 50 <= i <= 80:
    print("Batareya o‘rtacha, ehtiyot bo‘ling")
elif 20 <= i < 50:
    print("Batareya kam, zaryad qiling!")
elif i < 20:
    print("Batareya juda kam, darhol zaryad qiling!")
else:
    print("Noto‘g‘ri qiymat kiritildi!")
