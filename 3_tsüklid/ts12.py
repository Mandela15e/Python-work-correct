summa = 1000
aasta = 1

while aasta <= 10:
    summa = summa * 1.05
    print(aasta, ". aasta: ", round(summa, 2), " eurot", sep="")
    aasta = aasta + 1