oige_kasutajanimi = "e52"
oige_parool = "admin"

kasutajanimi = input("Sisesta kasutajanimi: ")

if kasutajanimi == oige_kasutajanimi:
    parool = input("Sisesta parool: ")
    if parool == oige_parool:
        print("Sisse logitud!")
    else:
        print("Vale parool")
else:
    print("Kasutajat pole")