def ruut(arv):
    return arv * arv


def ruutude_summa(a, b):
    return ruut(a) + ruut(b)


print(ruutude_summa(3, 4))
print(ruutude_summa(0, 5))
print(ruutude_summa(-2, 2))