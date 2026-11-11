arvud = [-12, 5, 0, 18, -7, 23, -3, 9]

positiivsed = 0
negatiivsed = 0
nullid = 0
positiivsete_summa = 0
negatiivsed_arvud = []

for arv in arvud:
    if arv > 0:
        positiivsed += 1
        positiivsete_summa += arv
    elif arv < 0:
        negatiivsed += 1
        negatiivsed_arvud.append(arv)
    else:
        nullid += 1

print("Positiivseid arve:", positiivsed)
print("Negatiivseid arve:", negatiivsed)
print("Nulle:", nullid)
print("Positiivsete arvude summa:", positiivsete_summa)
print("Negatiivsed arvud:", negatiivsed_arvud)