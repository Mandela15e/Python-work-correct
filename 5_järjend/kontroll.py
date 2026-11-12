nimed = []
punktid = []

with open("kontrolltoo.csv", encoding="utf-8") as fail:
    for rida in fail:
        rida = rida.strip()
        if rida == "":
            continue
        osad = rida.split(";")
        nimed.append(osad[0])
        punktid.append(int(osad[1]))


def hinne(p):
    if p >= 90:
        return 5
    elif p >= 75:
        return 4
    elif p >= 50:
        return 3
    elif p >= 20:
        return 2
    else:
        return 1


print("KONTROLLTÖÖ TULEMUSED")
print()
for i in range(len(nimed)):
    print(f"{i + 1}. {nimed[i]} – {punktid[i]} punkti")

kokku = len(nimed)
keskmine = sum(punktid) / kokku

parim = max(punktid)
halvim = min(punktid)
parimad = [nimed[i] for i in range(kokku) if punktid[i] == parim]
halvimad = [nimed[i] for i in range(kokku) if punktid[i] == halvim]

sooritas = 0
ei_sooritanud = 0
for p in punktid:
    if p >= 50:
        sooritas += 1
    else:
        ei_sooritanud += 1

print()
print("KONTROLLTÖÖ STATISTIKA")
print()
print("Õpilasi kokku:", kokku)
print("Keskmine punktisumma:", round(keskmine, 2))
print("Parim tulemus:", ", ".join(parimad), "–", parim, "punkti")
print("Madalaim tulemus:", ", ".join(halvimad), "–", halvim, "punkti")
print("Kontrolltöö sooritas:", sooritas, "õpilast")
print("Kontrolltööd ei sooritanud:", ei_sooritanud, "õpilast")

print()
print("HINDED")
print()
for i in range(kokku):
    print(f"{nimed[i]} – {punktid[i]} punkti – hinne {hinne(punktid[i])}")

print()
print("ÕPILASE OTSIMINE")
otsitav = input("Sisesta õpilase nimi: ").strip().lower()

leitud = False
for i in range(kokku):
    if nimed[i].lower() == otsitav:
        print("Õpilane:", nimed[i])
        print("Punktid:", punktid[i])
        print("Hinne:", hinne(punktid[i]))
        leitud = True
        break

if not leitud:
    print("Sellist õpilast ei leitud.")