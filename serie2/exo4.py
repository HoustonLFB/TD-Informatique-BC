somme = 0
produit = 1
cpt = 0

for v in range(1,100000):
    b = str(v)
    for i in b:
        somme = somme + int(i)
        produit = produit * int(i)
    if somme == produit:
        cpt = cpt + 1
        print(v)
    
    somme = 0
    produit = 1

print(cpt)