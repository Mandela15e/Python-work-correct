arv = 100

def muuda():
    arv = 20
    print("Funktsioonis:", arv)

muuda()
print("Põhiprogrammis:", arv)
 #Ennustus Funktsioonis 20 põhiprogramis 100
 #Funktsiooni sees tekitab rida arv = 20 uue lokaalse muutuja, see ei muuda põhiprogrammi muutujat arv = 100.
 # Lokaalne muutuja kaob funktsiooni lõppedes, seega on põhiprogrammis arv endiselt 100.