def lettreToRang(lettre):
    return ord(lettre) - ord("a")

def rangToLettre(rang):
    return chr(ord('a') + rang)

def manipulation_cle(texte, cle):
    cle_repetee = ""
    for i in range(len(texte) // len(cle)):
        cle_repetee += cle
    for i in range(len(texte) % len(cle)):
        cle_repetee += cle[:i]
    return cle_repetee

message = input("message ?")
message = message.lower()
message = message.replace(" ", "")

cle = input("clé ?")
cle = cle.lower()

code = ""
index = 0

for j in message:
    index = index % (len(cle))
    i = cle[index]

    rangI = lettreToRang(i)
    rangJ = lettreToRang(j)
        
    codeRang = (rangI + rangJ)%26
    codeLettre = rangToLettre(codeRang)

    code += codeLettre
    index = index + 1
print(code)




