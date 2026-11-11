i = 0

while i < 5:
    print(i)
    i=i + 1

    ##muutuja i algväärtus on 0
    ##Tsükli jätkumise tingimus on i < 5.Kui see on tõene,t
    ##täidetakse tsükli sisu uuesti
    ##Pärast tsükli lõppu on i väärtus 5. Viimasel kordusel (kui i oli 4) prinditakse 4 ja seejärel muutub i väärtuseks 5. 
    ##Tingimus 5 < 5 on väär, seega tsükkel lõpeb. Number 5 ise ei prindita, sest print tuleb enne suurendamist.
    
    