import math

def lettreToRang(lettre):
    return ord(lettre) - ord("a")

def rangToLettre(rang):
    return chr(ord('a') + rang)

def verifClef(clef):
    pgcd = math.gcd(clef, 26)

    if pgcd == 1:
        print("Clé valide")
    else:
        print("Clé invalide")
    
def chiffrement(texte, clef1, clef2):
    texteChiffre = ""
    texte = texte.lower().replace(" ", "")
    for lettre in texte:
        rang = lettreToRang(lettre)
        rangChiffre = (clef1 * rang + clef2) %26
        texteChiffre = texteChiffre + rangToLettre(rangChiffre)
    return texteChiffre

def codeDechiffrement(cle):
    for i in range(26):
        if (cle * i) % 26 == 1:
            return i

def dechiffrement(texte, a, b):
    textDechiffre = ""
    for lettre in texte:
        rang = lettreToRang(lettre)
        rangChiffre = (a * (rang-b))%26
        textDechiffre = textDechiffre + rangToLettre(rangChiffre)
    return textDechiffre

texte = "bonjour"
cle1 = 3
cle2 = 10

verifClef(cle1)

textChiffre = chiffrement(texte, cle1, cle2)

cle1Prime = codeDechiffrement(cle1)

print(dechiffrement(textChiffre,cle1Prime,cle2))