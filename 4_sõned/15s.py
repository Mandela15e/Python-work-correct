tekst = input("Sisesta tekst: ")

taishaalikke = 0
numbreid = 0

for m in tekst.lower():
    if m in "aeiouõäöü":
        taishaalikke += 1
    if m.isdigit():
        numbreid += 1

print()
print("Tähemärke kokku:", len(tekst))
print("Tähemärke ilma tühikuteta:", len(tekst.replace(" ", "")))
print("Sõnu:", len(tekst.split()))
print("Täishäälikuid:", taishaalikke)
print("Numbreid:", numbreid)