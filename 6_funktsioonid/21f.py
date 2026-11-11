def liida(a, b):
    return a + b


def lahuta(a, b):
    return a - b


def korruta(a, b):
    return a * b


def jaga(a, b):
    if b == 0:
        return None
    return a / b


def kuva_menuu():
    print()
    print("=== Taskukalkulaator ===")
    print("1. Liitmine")
    print("2. Lahutamine")
    print("3. Korrutamine")
    print("4. Jagamine")
    print("0. Lõpeta")


def küsi_arv(tekst):
    while True:
        try:
            return float(input(tekst).replace(",", "."))
        except ValueError:
            print("Palun sisesta korrektne arv.")


def kuva_tulemus(tulemus):
    if tulemus is None:
        print("Viga: nulliga jagada ei saa.")
    else:
        print(f"Tulemus: {tulemus:g}")


def main():
    while True:
        kuva_menuu()
        valik = input("Vali tehe (0-4): ").strip()

        if valik == "0":
            print("Head aega!")
            break

        if valik not in ("1", "2", "3", "4"):
            print("Tundmatu valik, proovi uuesti.")
            continue

        a = küsi_arv("Sisesta esimene arv: ")
        b = küsi_arv("Sisesta teine arv: ")

        if valik == "1":
            tulemus = liida(a, b)
        elif valik == "2":
            tulemus = lahuta(a, b)
        elif valik == "3":
            tulemus = korruta(a, b)
        else:
            tulemus = jaga(a, b)

        kuva_tulemus(tulemus)


main()