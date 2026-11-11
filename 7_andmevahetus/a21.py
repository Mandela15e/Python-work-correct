#!/usr/bin/env python3
import re
from collections import Counter

TULEMUSFAIL = "tekstianaluus.txt"
SONA_MUSTER = re.compile(r"[^\W\d_]+(?:[-'][^\W\d_]+)*")


def loe_fail(nimi):
    for kodeering in ("utf-8", "cp1257", "latin-1"):
        try:
            with open(nimi, "r", encoding=kodeering) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError("utf-8", b"", 0, 1, "Faili kodeeringut ei tuvastatud")


def küsi_tekst():
    while True:
        nimi = input("Sisesta analüüsitava tekstifaili nimi: ").strip().strip('"')
        if not nimi:
            print("Faili nimi ei tohi olla tühi.")
            continue
        try:
            tekst = loe_fail(nimi)
        except FileNotFoundError:
            print(f"Viga: faili '{nimi}' ei leitud.")
            continue
        except (OSError, UnicodeDecodeError) as viga:
            print(f"Viga faili lugemisel: {viga}")
            continue
        if not SONA_MUSTER.search(tekst):
            print("Fail ei sisalda ühtegi sõna.")
            continue
        return nimi, tekst


def loe_lauseid(tekst):
    osad = re.split(r"[.!?]+", tekst)
    return sum(1 for osa in osad if re.search(r"[^\W\d_]", osa))


def analüüsi(tekst):
    sonad = SONA_MUSTER.findall(tekst)
    pikim = max(sonad, key=len)
    sagedused = Counter(s.lower() for s in sonad)
    return {
        "sonu": len(sonad),
        "lauseid": loe_lauseid(tekst),
        "pikim": pikim,
        "top5": sagedused.most_common(5),
    }


def koosta_aruanne(failinimi, tulemus):
    read = [
        "TEKSTIANALÜÜSI TULEMUSED",
        "=" * 24,
        f"Analüüsitud fail: {failinimi}",
        f"Sõnade arv: {tulemus['sonu']}",
        f"Lausete ligikaudne arv: {tulemus['lauseid']}",
        f"Pikim sõna: {tulemus['pikim']} ({len(tulemus['pikim'])} tähte)",
        "",
        "Viis kõige sagedamini esinevat sõna:",
    ]
    for i, (sona, arv) in enumerate(tulemus["top5"], 1):
        read.append(f"  {i}. {sona} - {arv}")
    return "\n".join(read)


def main():
    failinimi, tekst = küsi_tekst()
    aruanne = koosta_aruanne(failinimi, analüüsi(tekst))
    print()
    print(aruanne)
    with open(TULEMUSFAIL, "w", encoding="utf-8") as f:
        f.write(aruanne + "\n")
    print(f"\nTulemused salvestati faili {TULEMUSFAIL}.")


if __name__ == "__main__":
    main()
