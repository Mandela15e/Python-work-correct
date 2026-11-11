fail = open("ostunimekiri.txt", "a", encoding="utf-8")

while True:
    toode = input("Sisesta toode: ").strip()
    if toode.upper() == "STOP":
        break
    fail.write(toode + "\n")

fail.close()

print()
print("Ostunimekiri salvestatud.")
print()

fail = open("ostunimekiri.txt", "r", encoding="utf-8")
print(fail.read())
fail.close()