fail = open("tekst.txt", "r", encoding="utf-8")

kirjavahemärgid = ".,!?;:-\"'()"
pikim = ""

for rida in fail:
    for sona in rida.split():
        sona = sona.strip(kirjavahemärgid)
        if len(sona) > len(pikim):
            pikim = sona

fail.close()

print(f"Kõige pikem sõna: {pikim}")
print(f"Pikkus: {len(pikim)}")