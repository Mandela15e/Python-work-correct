parool = input("Sisesta parool: ")

if len(parool) < 8:
    print("Parool on liiga lühike.")
elif len(parool) < 12:
    print("Parooli pikkus on sobiv.")
else:
    print("Parool on pikk.")