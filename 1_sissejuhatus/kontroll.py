nimi = input("Nimi: ")
vanus = int(input("Vanus: "))
pikkus_km = float(input("Koolitee: "))
aeg_min = int(input("Aeg minutites: "))

jargmine_vanus = vanus + 1
pikkus_m = int(pikkus_km * 1000)
tunnid = aeg_min // 60
minutid = aeg_min % 60
kiirus = pikkus_km / (aeg_min / 60)

print(f"Tere, {nimi}!")
print(f"Järgmisel aastal oled {jargmine_vanus}-aastane.")
print(f"Sinu koolitee pikkus on {pikkus_m} meetrit.")
print(f"Koolitee kestab {tunnid} tundi ja {minutid} minutit.")
print(f"Keskmine kiirus on {kiirus:.1f} km/h.")