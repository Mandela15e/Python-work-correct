#!/usr/bin/env python3
import os

ANDMEFAIL = "hinded.txt"
ARUANDEFAIL = "aruanne.txt"
ERISTAJA = ";"

MENUU = """
1. Kuva kõik õpilased
2. Lisa uus õpilane ja hinne
3. Otsi õpilast
4. Kuva hinnete statistika
5. Salvesta aruanne faili
6. Lõpeta
"""


def lae_andmed():
    opilased = []
    if not os.path.exists(ANDMEFAIL):
        return opilased
    with open(ANDMEFAIL, "r", encoding="utf-8") as f:
        for rida in f:
            rida = rida.strip()
            if not rida:
                continue
            nimi, _, hinne_tekst = rida.rpartition(ERISTAJA)
            try:
                hinne = int(hinne_tekst)
            except ValueError:
                continue
            if nimi.strip() and 1 <= hinne <= 5:
                opilased.append((nimi.strip(), hinne))
    return opilased


def lisa_faili(nimi, hinne):
    with open(ANDMEFAIL, "a", encoding="utf-8") as f:
        f.write(f"{nimi}{ERISTAJA}{hinne}\n")


def loe_hinne():
    while True:
        tekst = input("Hinne (1-5): ").strip()
        if tekst.isdigit() and 1 <= int(tekst) <= 5:
            return int(tekst)
        print("Viga: hinne peab olema täisarv vahemikus 1 kuni 5.")


def loe_nimi():
    while True:
        nimi = input("Õpilase nimi: ").strip().replace(ERISTAJA, " ")
        if nimi:
            return nimi
        print("Viga: nimi ei tohi olla tühi.")


def ridade_loend(opilased):
    return [f"{i}. {nimi} - {hinne}" for i, (nimi, hinne) in enumerate(opilased, 1)]


def statistika_read(opilased):
    if not opilased:
        return ["Andmed puuduvad, statistikat ei saa arvutada."]
    hinded = [hinne for _, hinne in opilased]
    keskmine = sum(hinded) / len(hinded)
    read = [
        f"Õpilasi kokku: {len(hinded)}",
        f"Hinnete keskmine: {keskmine:.2f}",
        "Hinnete esinemissagedus:",
    ]
    for h in range(1, 6):
        read.append(f"  Hinne {h}: {hinded.count(h)}")
    return read


def kuva_koik(opilased):
    if not opilased:
        print("Õpilasi pole veel lisatud.")
        return
    print("\nÕpilased:")
    print("\n".join(ridade_loend(opilased)))


def lisa_opilane(opilased):
    nimi = loe_nimi()
    hinne = loe_hinne()
    opilased.append((nimi, hinne))
    lisa_faili(nimi, hinne)
    print(f"Lisatud: {nimi} - {hinne}")


def otsi_opilast(opilased):
    paring = input("Otsitav nimi (või selle osa): ").strip().lower()
    if not paring:
        print("Otsingusõna on tühi.")
        return
    leitud = [(n, h) for n, h in opilased if paring in n.lower()]
    if not leitud:
        print("Sellist õpilast ei leitud.")
        return
    print(f"\nLeitud {len(leitud)}:")
    for nimi, hinne in leitud:
        print(f"{nimi} - {hinne}")


def kuva_statistika(opilased):
    print("\nHinnete statistika:")
    print("\n".join(statistika_read(opilased)))


def salvesta_aruanne(opilased):
    read = ["ÕPILASTE HINNETE ARUANNE", "=" * 26, ""]
    read += ridade_loend(opilased) if opilased else ["Õpilasi pole."]
    read += ["", "STATISTIKA"] + statistika_read(opilased)
    with open(ARUANDEFAIL, "w", encoding="utf-8") as f:
        f.write("\n".join(read) + "\n")
    print(f"Aruanne salvestati faili {ARUANDEFAIL}.")


def main():
    opilased = lae_andmed()
    tegevused = {
        "1": kuva_koik,
        "2": lisa_opilane,
        "3": otsi_opilast,
        "4": kuva_statistika,
        "5": salvesta_aruanne,
    }
    while True:
        print(MENUU)
        try:
            valik = input("Vali tegevus (1-6): ").strip()
        except EOFError:
            break
        if valik == "6":
            break
        tegevus = tegevused.get(valik)
        if tegevus is None:
            print("Tundmatu valik, sisesta number 1 kuni 6.")
            continue
        try:
            tegevus(opilased)
        except EOFError:
            break
    print("Head aega!")


if __name__ == "__main__":
    main()