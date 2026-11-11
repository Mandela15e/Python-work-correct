muugid = [125.50, 210.00, 98.75, 340.20, 185.40, 420.00, 275.90]
paevad = ["Esmaspäev", "Teisipäev", "Kolmapäev", "Neljapäev", "Reede", "Laupäev", "Pühapäev"]

print("Päevade müük:")
for i in range(len(muugid)):
    print(f"{paevad[i]}: {muugid[i]:.2f} €")

kogu = sum(muugid)
keskmine = kogu / len(muugid)

suurim_index = 0
ule_200 = 0
for i in range(len(muugid)):
    if muugid[i] > muugid[suurim_index]:
        suurim_index = i
    if muugid[i] > 200:
        ule_200 += 1

print()
print(f"Nädala kogumüük: {kogu:.2f} €")
print(f"Keskmine päevamüük: {keskmine:.2f} €")
print(f"Suurima müügiga päev: {paevad[suurim_index]} ({muugid[suurim_index]:.2f} €)")
print("Päevi müügiga üle 200 euro:", ule_200)