FAIL_SISSE = "tulemused.txt"
FAIL_VALJA = "aruanne.txt"


def loe_andmed(failinimi):
    nimed = []
    keskmised = []
    with open("tulemused.txt" , encoding="utf-8") as fail:
        for rida in fail:
            rida = rida.strip()
            if rida == "":
                continue
            osad = rida.split(";")
            tulemused = [int(t) for t in osad[1:4]]
            nimed.append(osad[0])
            keskmised.append(sum(tulemused) / len(tulemused))
    return nimed, keskmised


def arvuta_hinne(keskmine):
    if keskmine >= 90:
        return 5
    elif keskmine >= 75:
        return 4
    elif keskmine >= 60:
        return 3
    elif keskmine >= 50:
        return 2
    else:
        return 1


def koosta_aruanne(nimed, keskmised):
    hinded = [arvuta_hinne(k) for k in keskmised]
    klassi_keskmine = sum(keskmised) / len(keskmised)
    parim = nimed[keskmised.index(max(keskmised))]
    norgim = nimed[keskmised.index(min(keskmised))]
    positiivseid = len([h for h in hinded if h >= 3])

    read = ["ÕPILASTE TULEMUSTE ARUANNE", "-" * 30, ""]
    for i in range(len(nimed)):
        read.append(f"{nimed[i]:<10} Keskmine: {keskmised[i]:.2f}  Hinne: {hinded[i]}")
    read.append("")
    read.append("-" * 30)
    read.append(f"Klassi keskmine: {klassi_keskmine:.2f}")
    read.append(f"Parim õpilane: {parim}")
    read.append(f"Nõrgim õpilane: {norgim}")
    read.append(f"Positiivse hindega õpilasi: {positiivseid}")
    return read


def salvesta_aruanne(failinimi, read):
    with open(failinimi, "w", encoding="utf-8") as fail:
        fail.write("\n".join(read) + "\n")


def main():
    try:
        nimed, keskmised = loe_andmed(FAIL_SISSE)
    except FileNotFoundError:
        print(f"Viga: faili '{FAIL_SISSE}' ei leitud. Loo fail samasse kausta programmiga.")
        return
    except (ValueError, IndexError):
        print(f"Viga: faili '{FAIL_SISSE}' sisu on vigane.")
        return

    if len(nimed) == 0:
        print(f"Viga: fail '{FAIL_SISSE}' on tühi.")
        return

    read = koosta_aruanne(nimed, keskmised)
    for rida in read:
        print(rida)
    salvesta_aruanne(FAIL_VALJA, read)


main()