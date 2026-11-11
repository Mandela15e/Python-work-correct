ostukorv = []

for i in range(5):
    toode = input(f"Sisesta toode nr {i + 1}: ")
    ostukorv.append(toode)

print("Ostukorv:", ostukorv)
print("Toodete arv:", len(ostukorv))