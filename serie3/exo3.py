def convertBinaire(ip):
    binaire = ""
    octets = ip.split(".")
    for octet in octets:
        binaire = binaire + bin(int(octet))[2:].zfill(8)
    return binaire

adresse = input("Entrer IP : ")
masque = input("Entrer Masque : ")
reseau = input("Entrer adresse de réseau : ")

adresseBinaire = convertBinaire(adresse)
masqueBinaire = convertBinaire(masque)
reseauBinaire = convertBinaire(reseau)
reseauCalc = ""

#addition logique de l'adresse et du masque pour trouver l'adresse de réseau
for i in range(len(adresseBinaire)):
    if adresseBinaire[i] == "1" and masqueBinaire[i] == "1":
        reseauCalc = reseauCalc + "1"
    else:
        reseauCalc = reseauCalc + "0"

if reseauBinaire == reseauCalc:
    print("c'est ok")