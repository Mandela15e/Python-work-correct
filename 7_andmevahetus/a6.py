fail = open("tekst.txt", "w", encoding="utf-8")
fail.write("Python on populaarne programmeerimiskeel.\n")
fail.write("Python sobib hästi algajatele.\n")
fail.write("Failide töötlemine on oluline oskus.\n")
fail.close()

fail = open("tekst.txt", "r", encoding="utf-8")

arv = 0
for rida in fail:
    sonad = rida.split()
    arv += len(sonad)

fail.close()

print(f"Tekstis on {arv} sõna.")