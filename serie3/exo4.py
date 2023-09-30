def convertBinaire(ip):
    binaire = ""
    octets = ip.split(".")
    for octet in octets:
        binaire = binaire + bin(int(octet))[2:].zfill(8)
    return binaire

masque = input("Entrer un masque :  ")

masqueBinaire = convertBinaire(masque)

cpt = 0

#calcul de 0 à la fin du masque
for i in range(len(masqueBinaire)):
    if masqueBinaire[i] == "0":
        cpt = cpt + 1
    if cpt != "0" and masqueBinaire[i] == "1":
        print("ERREUR DANS LE MASQUE")

adressesTotales = 2**cpt
adressesDispo = adressesTotales - 2
print("Il y a " + str(adressesTotales) + " adresses totales mais " + str(adressesDispo) + " disponibles en enlevant le l'adrese de réseau et de diffusion.")