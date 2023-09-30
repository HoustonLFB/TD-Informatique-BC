def est_valide(ip):
    octets = ip.split(".")
    for i in octets:
        if int(i) < 0 or int(i) > 255:
            return False
    return True

ip = "192.55.1.1"

print(est_valide(ip))