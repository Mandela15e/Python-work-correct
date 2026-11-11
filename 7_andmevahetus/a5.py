fail = open("arvud.txt", "r", encoding="utf-8")

arvud = []
for rida in fail:
    rida = rida.strip()
    if rida != "":
        arvud.append(int(rida))

fail.close()

suurim = max(arvud)
vaikseim = min(arvud)

print(f"Suurim arv: {suurim}")
print(f"Väikseim arv: {vaikseim}")
print(f"Vahe: {suurim - vaikseim}")