arvud = []

with open("arvud.txt", encoding="utf-8") as fail:
    for rida in fail:
        arvud.append(int(rida.strip()))

print("Arvud:", arvud)
print("Suurim arv:", max(arvud))
print("Väikseim arv:", min(arvud))
print("Keskmine:", round(sum(arvud) / len(arvud), 2))
print("Kasvavas järjekorras:", sorted(arvud))