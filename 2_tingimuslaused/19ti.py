try:
    aasta = int(input("Sisesta aasta: "))
except ValueError:
    print("Palun sisesta aasta täisarvuna.")
else:
    if aasta % 400 == 0:
        print(f"{aasta} on liigaasta.")
    elif aasta % 4 == 0:
     print(f"{aasta} on liigiaasta.")
    else:
       print(f"{aasta} ei ole liigaasta.")
       