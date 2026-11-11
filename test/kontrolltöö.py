def raha_eurodes(kastide_arv, kilo_hind_sentides):
    return round(kastide_arv * 5 * (kilo_hind_sentides / 100), 1)


failinimi = input("Sisestage failinimi: ")
kilo_hind = int(input("Sisestage kilo hind sentides: "))

kokku = 0
paev = 1

fail = open(failinimi, encoding="utf-8")
for rida in fail:
    rida = rida.strip()
    if rida != "":
        kastid = int(rida)
        eurod = raha_eurodes(kastid, kilo_hind)
        print(str(paev) + ". päeval sai " + str(eurod) + " eurot.")
        kokku += eurod
        paev += 1
fail.close()

print("Kokku sai: " + str(round(kokku, 1)) + " eurot.")