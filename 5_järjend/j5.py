tahed = ["A", "B", "C", "D", "E", "F"]
print(tahed[1:4])  ##B,C,D
print(tahed[:3])   ##A,B,C
print(tahed[3:])   ##D,E,F
print(tahed[-3:-1]) ##D,E
print(tahed[::-1]) ##F,E,D,C,B,A

## Viilutamisel ei kaasata lõpuindeksiga elementi, sest vahemiku algus on kaasa arvatud, 
# aga lõpp mitte. Nii on elementide arv alati lõpp - 
# algus ja viilud tahed[:3] ning tahed[3:] annavad kokku terve järjendi ilma kattumiseta.