def celsius_fahrenheit(c):
    return c * 9 / 5 + 32


for kraadid in (0, 20, 37, 100):
    print(f"{kraadid} °C = {celsius_fahrenheit(kraadid)} °F")