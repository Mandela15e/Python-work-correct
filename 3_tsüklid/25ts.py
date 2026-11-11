hind = float(input("Sisesta hind: "))

tooteid = 0
kokku = 0

while hind != 0:
    tooteid = tooteid + 1
    kokku = kokku + hind
    hind = float(input("Sisesta hind: "))

print()
print("Tooteid:", tooteid)
print(f"Kokku: {kokku:.2f} €")