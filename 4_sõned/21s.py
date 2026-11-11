parool = input("Sisesta parool: ")

punktid = 0
puudu = []

if len(parool) >= 8:
    punktid += 1
else:
    puudu.append("Parool on liiga lühike (vähemalt 8 märki).")

suur = False
vaike = False
number = False
erimark = False

for m in parool:
    if m.isupper():
        suur = True
    elif m.islower():
        vaike = True
    elif m.isdigit():
        number = True
    elif m != " ":
        erimark = True

if suur:
    punktid += 1
else:
    puudu.append("Puudub suurtäht.")

if vaike:
    punktid += 1
else:
    puudu.append("Puudub väiketäht.")

if number:
    punktid += 1
else:
    puudu.append("Puudub number.")

if erimark:
    punktid += 1
else:
    puudu.append("Puudub erimärk.")

print()
print("Tulemus: " + str(punktid) + "/5")

if punktid <= 2:
    print("Hinnang: Nõrk parool")
elif punktid <= 4:
    print("Hinnang: Keskmine parool")
else:
    print("Hinnang: Kõik nõuded täidetud")

if len(puudu) > 0:
    print()
    for p in puudu:
        print(p)