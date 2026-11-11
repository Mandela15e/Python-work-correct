lause = input("Sisesta lause: ").lower()
taishaalikud = "aeiouõäöü"

kokku = 0
for taht in lause:
    if taht in taishaalikud:
        kokku += 1

print()
print("Täishäälikuid kokku:", kokku)

print()
print("Iga täishääliku esinemised:")
for h in taishaalikud:
    print(h + ":", lause.count(h))