import os

kaust = os.path.dirname(os.path.abspath(__file__))
sisend = os.path.join(kaust, "temperatuurid.txt")
valjund = os.path.join(kaust, "temperatuuri_aruanne.txt")

try:
    fail = open(sisend, "r", encoding="utf-8")
except FileNotFoundError:
    print("Faili temperatuurid.txt ei leitud kaustast:", kaust)
    raise SystemExit

paevad = []
temperatuurid = []

for rida in fail:
    osad = rida.split()
    if len(osad) < 2:
        continue
    try:
        temp = float(osad[-1].replace(",", "."))
    except ValueError:
        continue
    paevad.append(osad[0])
    temperatuurid.append(temp)

fail.close()

if len(temperatuurid) == 0:
    print("Failis pole ühtegi korrektset rida.")
    raise SystemExit

keskmine = sum(temperatuurid) / len(temperatuurid)

soojim = max(temperatuurid)
soojim_paev = paevad[temperatuurid.index(soojim)]

kulmim = min(temperatuurid)
kulmim_paev = paevad[temperatuurid.index(kulmim)]

ule_15 = 0
for temp in temperatuurid:
    if temp > 15:
        ule_15 += 1

fail = open(valjund, "w", encoding="utf-8")
fail.write("Nädala temperatuuriaruanne\n")
fail.write("--------------------------\n")
fail.write(f"Keskmine temperatuur: {keskmine:.2f} kraadi\n")
fail.write(f"Kõige soojem päev: {soojim_paev} ({soojim:g} kraadi)\n")
fail.write(f"Kõige külmem päev: {kulmim_paev} ({kulmim:g} kraadi)\n")
fail.write(f"Päevi üle 15 kraadi: {ule_15}\n")
fail.close()

print("Aruanne salvestatud faili temperatuuri_aruanne.txt")S