def valide(chaine):
    if chaine == "":
        return False
    for i in chaine:
        if i == "a" or i == "t" or i == "g" or i == "c":
            pass
        else:
            return False
    return True

def seqInChaine(sequence, chaine):
    if sequence in chaine:
        return True
    else:
        return False
    
def main():
    sequence = "attggcgtct"
    chaine = "atgctgcattggcgtctatgctggtcgtca"

    if valide(sequence) and valide(chaine):
        print("séquence et chaine sont valides")
        if seqInChaine(sequence, chaine):
            print("la séquence se trouve dans la chaine")

main()

