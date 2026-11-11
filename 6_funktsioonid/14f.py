def taishaalikuid(tekst):
    taishaalikud = "aeiouõäöü"
    arv = 0
    for taht in tekst.lower():
        if taht in taishaalikud:
            arv += 1
    return arv


print(taishaalikuid("Tere"))
print(taishaalikuid("Õunapuu"))
print(taishaalikuid("PÜHAPÄEV"))
print(taishaalikuid("Kristjan"))
print(taishaalikuid(""))