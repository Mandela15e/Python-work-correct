epost = input("Sisesta e-post: ")

if " " in epost:
    print("Viga: aadress ei tohi sisaldada tühikuid.")
elif epost.count("@") != 1:
    print("Viga: aadress peab sisaldama täpselt ühte @ märki.")
else:
    kasutaja, domeen = epost.split("@")

    if len(kasutaja) == 0:
        print("Viga: @ ees peab olema vähemalt üks tähemärk.")
    elif "." not in domeen:
        print("Viga: domeenis peab olema punkt.")
    elif domeen.startswith(".") or domeen.endswith("."):
        print("Viga: domeen ei tohi alata ega lõppeda punktiga.")
    else:
        print("Aadressi kuju on sobiv.")