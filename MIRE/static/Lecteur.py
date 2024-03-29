def lecture():
    f = open("Board145.txt", "r")
    valeur = f.read()
    f.close()
    val = valeur.split(":")
    val[1].split("=")
    return val
