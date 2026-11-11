küsimus = int(input("sisesta vanus:"))
pilet = 10
sooduspilet = 6
if küsimus < 18 or küsimus > 65:
    print("piletihind on", sooduspilet, "eurot")
else:
   print("piletihind on " , pilet, "eurot")