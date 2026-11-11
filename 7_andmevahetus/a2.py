fail = open("tervitus.txt", "r", encoding="utf-8")

for number, rida in enumerate(fail, start=1):
    print(f"{number}: {rida.strip()}")

fail.close()