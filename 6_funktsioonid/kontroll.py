def kuva_menuu():
    print("=================================")
    print("     ÕPILASTE HINNETE SÜSTEEM")
    print("=================================")
    print()
    print("1. Lisa õpilane")
    print("2. Kuva kõik õpilased")
    print("3. Kuva klassi statistika")
    print("4. Otsi õpilast nime järgi")
    print("0. Välju")
    print()


def arvuta_hinne(punktid):
    if punktid >= 90:
        return 5
    elif punktid >= 75:
        return 4
    elif punktid >= 50:
        return 3
    elif punktid >= 20:
        return 2
    else:
        return 1


def leia_indeks(nimed, nimi):
    for i in range(len(nimed)):
        if nimed[i].lower() == nimi.lower():
            return i
    return -1


def lisa_opilane(nimed, punktid, nimi, tulemus):
    if leia_indeks(nimed, nimi) != -1:
        return False
    nimed.append(nimi)
    punktid.append(tulemus)
    return True


def leia_keskmine(punktid):
    if len(punktid) == 0:
        return 0
    return sum(punktid) / len(punktid)


def leia_parim(nimed, punktid):
    if len(punktid) == 0:
        return None, None
    parim = max(punktid)
    return nimed[punktid.index(parim)], parim


def leia_norgim(nimed, punktid):
    if len(punktid) == 0:
        return None, None
    norgim = min(punktid)
    return nimed[punktid.index(norgim)], norgim


def otsi_opilane(nimed, punktid, nimi):
    i = leia_indeks(nimed, nimi)
    if i == -1:
        return None, None
    return nimed[i], punktid[i]


def kuva_opilased(nimed, punktid):
    if len(nimed) == 0:
        print("Õpilasi pole veel lisatud.")
        return
    print()
    for i in range(len(nimed)):
        print(f"{i + 1}. {nimed[i]} – {punktid[i]} punkti – hinne {arvuta_hinne(punktid[i])}")


def kuva_statistika(nimed, punktid):
    if len(nimed) == 0:
        print("Statistikat ei saa kuvada, sest õpilasi pole lisatud.")
        return

    parim_nimi, parim_punktid = leia_parim(nimed, punktid)
    norgim_nimi, norgim_punktid = leia_norgim(nimed, punktid)

    jaotus = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
    for p in punktid:
        jaotus[arvuta_hinne(p)] += 1

    print()
    print("=================================")
    print("       KLASSI STATISTIKA")
    print("=================================")
    print()
    print("Õpilasi kokku:", len(nimed))
    print(f"Keskmine punktisumma: {leia_keskmine(punktid):.2f}")
    print(f"Parim tulemus: {parim_nimi} ({parim_punktid} p)")
    print(f"Nõrgim tulemus: {norgim_nimi} ({norgim_punktid} p)")
    print()
    print("Hinnete jaotus:")
    for hinne in [5, 4, 3, 2, 1]:
        arv = jaotus[hinne]
        sona = "õpilane" if arv == 1 else "õpilast"
        print(f"Hinne {hinne}: {arv} {sona}")


def küsi_punktid(min_punktid=0, max_punktid=100):
    while True:
        sisend = input(f"Sisesta punktisumma ({min_punktid}-{max_punktid}): ").strip()
        try:
            punktid = int(sisend)
        except ValueError:
            print("Palun sisesta täisarv.")
            continue
        if min_punktid <= punktid <= max_punktid:
            return punktid
        print(f"Punktisumma peab olema vahemikus {min_punktid}-{max_punktid}.")


def lisa_kasutajalt(nimed, punktid):
    nimi = input("Sisesta õpilase nimi: ").strip()
    if nimi == "":
        print("Nimi ei tohi olla tühi.")
        return
    if leia_indeks(nimed, nimi) != -1:
        print("Sellise nimega õpilane on juba olemas.")
        return
    tulemus = küsi_punktid()
    lisa_opilane(nimed, punktid, nimi, tulemus)
    print(f"Õpilane {nimi} lisati.")


def otsi_kasutajalt(nimed, punktid):
    nimi = input("Sisesta õpilase nimi: ").strip()
    leitud_nimi, leitud_punktid = otsi_opilane(nimed, punktid, nimi)
    if leitud_nimi is None:
        print("Sellist õpilast ei leitud.")
    else:
        print("Õpilane:", leitud_nimi)
        print("Punktid:", leitud_punktid)
        print("Hinne:", arvuta_hinne(leitud_punktid))


def main():
    nimed = []
    punktid = []

    while True:
        print()
        kuva_menuu()
        valik = input("Vali tegevus: ").strip()

        if valik == "1":
            lisa_kasutajalt(nimed, punktid)
        elif valik == "2":
            kuva_opilased(nimed, punktid)
        elif valik == "3":
            kuva_statistika(nimed, punktid)
        elif valik == "4":
            otsi_kasutajalt(nimed, punktid)
        elif valik == "0":
            print("Programm lõpetatud.")
            break
        else:
            print("Vigane valik, proovi uuesti.")


main()