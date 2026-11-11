import os

kaust = os.path.dirname(os.path.abspath(__file__))
sisend = os.path.join(kaust, "kontaktid.txt")

fail = open(sisend, "r", encoding="utf-8")

kontaktid = []
for rida in fail:
    rida = rida.strip()
    if rida == "":
        continue
    osad = rida.split(";")
    if len(osad) < 3:
        continue
    kontaktid.append((osad[0], osad[1], osad[2]))

fail.close()

while True:
    otsing = input("Sisesta nimi (lõpetamiseks STOP): ").strip()

    if otsing.lower() == "stop":
        break

    leitud = False
    for nimi, email, telefon in kontaktid:
        if nimi.lower() == otsing.lower():
            print(f"E-post: {email}")
            print(f"Telefon: {telefon}")
            leitud = True
            break

    if not leitud:
        print("Kontakti ei leitud.")

    print()

print("Head aega!")