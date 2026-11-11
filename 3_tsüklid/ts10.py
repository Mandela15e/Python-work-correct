oige_parool = "python123"
katsed = 0
lubatud = False

while katsed < 3 and not lubatud:
    parool = input("Sisesta parool: ")
    katsed = katsed + 1

    if parool == oige_parool:
        lubatud = True
    else:
        print("Vale parool!")

if lubatud:
    print("Ligipääs lubatud!")
else:
    print("Ligipääs blokeeritud!")