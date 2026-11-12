
nimi = input("Sisesta enda nimi: ")

punktid = int(input("Sisesta palju punkte said: "))

if punktid >= 90:
    print("5")
elif punktid >= 75 and punktid < 90:
    print("4")
elif punktid >= 50 and punktid < 75:
    print("3")
elif punktid > 20 and punktid < 50:
    print("2")
    print("hoiatus")
elif punktid > 0 and punktid <= 20:
    print("1")
    print("hoiatus")
else:
    print("Vigane punktide arv!")

puudumised = int(input("Puudumiste arv: "))

if puudumised != 10 and puudumised >= 10:
    print("hoiatus")
else:
    print("Puudumisi on lubatud piirides")

tööd = input("Kas esitasid kõik tööd? (jah/ei): ")

if tööd == "jah":
    print("Tubli! Kõik tööd esitatud")
else:
    print("Kõik tööd ei ole esitatud")

if tööd == "jah" or puudumised < 10:
    print("Üks tingimustest on täidetud")
