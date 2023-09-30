binaire = ""
ip = "192.168.1.10"
octets = ip.split(".")
for octet in octets:
    binaire = binaire + bin(int(octet))[2:].zfill(8)

print(binaire)