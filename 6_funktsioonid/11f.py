def suurim(a, b, c):
    tulemus = a
    if b > tulemus:
        tulemus = b
    if c > tulemus:
        tulemus = c
    return tulemus


print(suurim(3, 9, 5))
print(suurim(10, 2, 7))
print(suurim(1, 4, 8))

print(suurim(6, 6, 2))
print(suurim(2, 7, 7))
print(suurim(5, 5, 5))

print(suurim(-3, -1, -8))