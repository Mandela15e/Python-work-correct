hinded = [4, 5, 3, 4, 2, 5, 5, 3, 4, 5, 2, 4]

print("Hinnete koguarv:", len(hinded))
print("Keskmine hinne:", round(sum(hinded) / len(hinded), 2))

esinemised = []
for hinne in range(1, 6):
    esinemised.append(hinded.count(hinne))

suurim = max(esinemised)
sagedased = []
for hinne in range(1, 6):
    if esinemised[hinne - 1] == suurim:
        sagedased.append(hinne)
print("Kõige sagedamini esinevad hinded:", sagedased, f"({suurim} korda)")

positiivsed = 0
mitterahuldavad = 0
for hinne in hinded:
    if hinne >= 3:
        positiivsed += 1
    else:
        mitterahuldavad += 1
print("Positiivseid hindeid (3-5):", positiivsed)
print("Mitterahuldavaid hindeid (1-2):", mitterahuldavad)

print()
print("Esinemiste arv:")
for hinne in range(1, 6):
    print(f"Hinne {hinne}: {esinemised[hinne - 1]} korda")

print()
print("Jaotus:")
for hinne in range(1, 6):
    print(f"Hinne {hinne}: {'*' * esinemised[hinne - 1]}")