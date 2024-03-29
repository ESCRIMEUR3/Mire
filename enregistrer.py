import serial
import time

# Création de l'objet Serial sans l'ouvrir immédiatement
"""val1 = serial.Serial(
    port='COM4',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
) """ # Augmentation du timeout pour éviter des erreurs de lecture

val2 = serial.Serial(
    port='COM7',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1  # Augmentation du timeout pour éviter des erreurs de lecture
)

#val1.flushInput()
val2.flushInput()  # Utiliser flushInput() pour vider le tampon d'entrée

# Affichage des données lues
valeur2 = val2.readline().strip()  # Lire une ligne (jusqu'au prochain '\n') et enlever les caractères de nouvelle ligne
valeur2 = valeur2.decode('ascii')
ID_Board = valeur2.split(':')

f = open("Board" + ID_Board[0] + ".txt", "w")
while True:
    """
    valeur1 = val1.readline().strip()  # Lire une ligne (jusqu'au prochain '\n') et enlever les caractères de nouvelle ligne
    valeur1 = valeur1.decode('ascii')  # Déchiffrer les octets en chaîne ASCII
    print(valeur1)
    """
    valeur2 = val2.readline().strip()  # Lire une ligne (jusqu'au prochain '\n') et enlever les caractères de nouvelle ligne
    valeur2 = valeur2.decode('ascii')  # Déchiffrer les octets en chaîne ASCII
    print(valeur2, '\n')
    f.write(valeur2 + "\n")
    f.close()
    time.sleep(2)
    f = open("Board" + ID_Board[0] + ".txt", "w")

# Fermeture du port série
#val1.close()
val2.close()
f.close()