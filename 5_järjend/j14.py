sonad = ["arvuti", "programmeerimine", "hiir", "klaviatuur", "monitor"]

pikim = sonad[0]
lyhim = sonad[0]

for sona in sonad:
    if len(sona) > len(pikim):
        pikim = sona
    if len(sona) < len(lyhim):
        lyhim = sona

print(f"Kõige pikem sõna: {pikim} ({len(pikim)} tähemärki)")
print(f"Kõige lühem sõna: {lyhim} ({len(lyhim)} tähemärki)")