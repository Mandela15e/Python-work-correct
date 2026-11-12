
kokku_sisestasid = 0
summa = 0
paaris_kokku = 0
paaritu_kokku = 0
postiivseid = 0
negatiivseid = 0
while True:
    arv = int(input("Sisesta uus arv (0 lõpetab): ")) 
    summa = summa + arv
    if arv == 0:
        break
    kokku_sisestasid += 1
    keskmine = summa / kokku_sisestasid
    if arv % 2 == 0:
        paaris_kokku += 1
    else:
        paaritu_kokku += 1
    if arv >0:
        postiivseid += 1
    else:
        negatiivseid += 1



    print("Programm lõpetatud!")
print("Sisestatud arve: ", kokku_sisestasid)
print("Summa: ", summa)
print("Keskmine: ", keskmine)
print("paarisarve: ", paaris_kokku)
print("paarituid: ", paaritu_kokku)
print("positiivseid: ", postiivseid)
print("negatiivseid: ", negatiivseid)