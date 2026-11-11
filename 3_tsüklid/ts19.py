from random import randint

salajane = randint(1, 100)

arvamus = int(input("Arva arv 1–100: "))

while arvamus != salajane:
    if arvamus > salajane:
        print("Salajane arv on väiksem.")
    else:
        print("Salajane arv on suurem.")
    arvamus = int(input("Arva arv 1–100: "))

print("Õige!")