päevi = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

kuu = int(input("Sisesta kuu: "))
kuupäev = int(input("Sisesta kuupäev: "))

if 1 <= kuu <= 12 and 1 <= kuupäev <= päevi[kuu - 1]:
    print("see on võimalik kuupäev")
else:
    print("see ei ole võimalik kuupäev")