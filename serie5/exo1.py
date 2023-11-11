tab = [7,7,7,7,7,5,5,5,5,1,1,3,3,1,2,2,4,4,4,5,5,5,5,5]

def premierPlateau(m):

    v = 0
    j = 0

    for i in range (0, len(tab)):
        if v == 0:
            v = tab[i]
            j = 1
        if v == tab[i]:
            j = j + 1
    j = j -1

    return [v,j]

premier = premierPlateau(tab)

print(premier)
