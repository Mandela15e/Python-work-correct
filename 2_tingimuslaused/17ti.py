a = float(input("sisesta  esimese külje pikkus:"))
b = float(input("sisesta  teise külje pikkus:"))
c = float(input("sisesta kolmanda külje pikkus:"))
if a + b > c and a + c >b and b + c >a:
    print("Kolmnurk on võimalik")
else:
    print("Kolmnurk ei ole võimalik")