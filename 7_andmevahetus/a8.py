nimi = input("Sisesta nimi: ")
vanus = input("Sisesta vanus: ")
email = input("Sisesta e-posti aadress: ")

fail = open("kasutaja.txt", "w", encoding="utf-8")
fail.write(nimi + "\n")
fail.write(vanus + "\n")
fail.write(email + "\n")
fail.close()

fail = open("kasutaja.txt", "r", encoding="utf-8")
sisu = fail.read()
fail.close()

print()
print("Faili sisu:")
print(sisu)