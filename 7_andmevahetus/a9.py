fail = open("ostunimekiri.txt", "w", encoding="utf-8")

while True:
    toode = input("Sisesta toode: ")
    if toode == "STOP":
        break
    fail.write(toode + "\n")

fail.close()

print()
print("Ostunimekiri salvestatud.")