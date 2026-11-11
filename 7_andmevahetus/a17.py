import os

kaust = os.path.dirname(os.path.abspath(__file__))
sisend = os.path.join(kaust, "muugiaruanne.txt")

fail = open(sisend, "r", encoding="utf-8")

kogu_tulu = 0
parim_toode = ""
parim_tulu = 0

print("Müügitulu toodete kaupa:")

for rida in fail:
    osad = rida.split()
    if len(osad) < 3:
        continue

    nimi = osad[0]
    hind = float(osad[1])
    kogus = int(osad[2])

    tulu = hind * kogus
    kogu_tulu += tulu

    print(f"{nimi}: {tulu:.2f} €")

    if tulu > parim_tulu:
        parim_tulu = tulu
        parim_toode = nimi

fail.close()

print()
print(f"Kogu müügitulu: {kogu_tulu:.2f} €")
print(f"Suurima müügituluga toode: {parim_toode} ({parim_tulu:.2f} €)")