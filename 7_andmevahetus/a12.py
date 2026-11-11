fail = open("sisestatud_arvud.txt", "w", encoding="utf-8")

for i in range(5):
    arv = int(input(f"Sisesta arv {i + 1}: "))
    fail.write(str(arv) + "\n")

fail.close()

fail = open("sisestatud_arvud.txt", "r", encoding="utf-8")

arvud = []
for rida in fail:
    arvud.append(int(rida.strip()))

fail.close()

summa = sum(arvud)
keskmine = summa / len(arvud)

print()
print("Sisestatud arvud: " + ", ".join(str(arv) for arv in arvud))
print(f"Summa: {summa}")
print(f"Keskmine: {keskmine}")