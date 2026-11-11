import math
import os

kaust = os.path.dirname(os.path.abspath(__file__))
sisend = os.path.join(kaust, "mootmised.txt")
valjund = os.path.join(kaust, "korrektsed_mootmised.txt")

try:
    fail = open(sisend, "r", encoding="utf-8")
except FileNotFoundError:
    print("Faili mootmised.txt ei leitud kaustast:", kaust)
    raise SystemExit

korrektsed = []
vigaseid = 0

for rida in fail:
    rida = rida.strip()
    if rida == "":
        continue
    try:
        arv = float(rida.replace(",", "."))
    except ValueError:
        vigaseid += 1
        continue
    if not math.isfinite(arv):
        vigaseid += 1
        continue
    korrektsed.append(arv)

fail.close()

fail = open(valjund, "w", encoding="utf-8")
for arv in korrektsed:
    fail.write(f"{arv:g}\n")
fail.close()

print(f"Kehtivaid väärtusi: {len(korrektsed)}")
print(f"Vigaseid kirjeid: {vigaseid}")

if len(korrektsed) > 0:
    keskmine = sum(korrektsed) / len(korrektsed)
    print(f"Keskmine: {keskmine:.2f}")
else:
    print("Keskmist ei saa arvutada, sest kehtivaid väärtusi pole.")