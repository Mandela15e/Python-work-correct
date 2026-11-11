arv = 0
summa = 0

with open("arvud.txt", encoding="utf-8") as fail:
    for rida in fail:
        summa += int(rida.strip())
        arv += 1

print("Arvude arv:", arv)
print("Arvude summa:", summa)