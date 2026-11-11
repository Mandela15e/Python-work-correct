fail = open("arvud.txt", "r", encoding="utf-8")

paaris = 0
paaritu = 0

for rida in fail:
    rida = rida.strip()
    if rida == "":
        continue
    arv = int(rida)
    if arv % 2 == 0:
        paaris += 1
    else:
        paaritu += 1

fail.close()

print(f"Paarisarve: {paaris}")
print(f"Paarituid arve: {paaritu}")