arvud = [4, 8, 12, 16, 20]
print(arvud[0])   ## prindib 4
print(arvud[-1])  ## prindib 20
print(arvud[2] + arvud[3])  ## prindib 28
print(arvud[len(arvud) - 2]) ## prindib 16
print(arvud[1] * 2) ##prindib 16

##Kuna viimase elemendi indeks on len(arvud) - 1, on eelviimase indeks sellest üks võrra väiksem ehk len(arvud) - 2, mis on siin 5 - 2 = 3 ja arvud[3] on 16.