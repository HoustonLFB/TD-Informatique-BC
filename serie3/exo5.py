from textwrap import wrap

def convertBinaire(ip):
    binaire = ""
    octets = ip.split(".")
    for octet in octets:
        binaire = binaire + bin(int(octet))[2:].zfill(8)
    return binaire

def convertDecimal(ip):
    adresse = ""
    octets = wrap(ip, 8)
    for octet in octets:
        adresse = adresse + str(int(octet, 2)) + "."
    
    adresse = adresse[:-1]
    return adresse


def adresseReseau(ip, masque):
    adresseBinaire = convertBinaire(adresse)
    masqueBinaire = convertBinaire(masque)

    reseauCalc = ""
    for i in range(len(adresseBinaire)):
        if adresseBinaire[i] == "1" and masqueBinaire[i] == "1":
            reseauCalc = reseauCalc + "1"
        else:
            reseauCalc = reseauCalc + "0"
    
    return reseauCalc

def premiereAdresse(reseau):
    premAdresse = reseau[:-1] + "1"

    return premAdresse

def bitZeroMasque(masqueBinaire):
    cpt = 0
    for i in range(len(masqueBinaire)):
        if masqueBinaire[i] == "0":
            cpt = cpt + 1
    return cpt

def diffusionAdresse(resBinaire, masBinaire):
    bitZero = bitZeroMasque(masBinaire)
    resBinaire = resBinaire[:-bitZero]
    diffusion = resBinaire + bitZero*"1"

    return diffusion

def lastAdresse(ip):
    ip = ip[:-1]
    ip = ip + "0"
    return ip

#adresse = input("Entrer IP : ")
#masque = input("Entrer Masque : ")
adresse = "192.168.52.0"
masque = "255.255.255.252"

adresseBinaire = convertBinaire(adresse)
masqueBinaire = convertBinaire(masque)
reseauBinaire = adresseReseau(adresse, masque)

reseau = convertDecimal(reseauBinaire)
premiereAdresseBinaire = premiereAdresse(reseauBinaire)
premAdresse = convertDecimal(premiereAdresseBinaire)
diffAdresseBinaire = diffusionAdresse(reseauBinaire, masqueBinaire)
diffAdresse = convertDecimal(diffAdresseBinaire)
derniereAdresseBinaire = lastAdresse(diffAdresseBinaire)
derniereAdresse = convertDecimal(derniereAdresseBinaire)

print("Addresse de réseau : " + reseau)
print("Première addresse hôte : " + premAdresse)
print("Dernière adresse hôte : " + derniereAdresse)
print("Adresse de diffusion : " + diffAdresse)