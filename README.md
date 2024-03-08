# projet_m-t-o
# le projet méteo et t'un projet visent a fabriqué une météo modulable et pour toute conditions  

# Systeme d'identificcation des modules

J'utilise le même principe que pour le **Multiplexer** et le **demultiplexer**, pour faire simple :

1. Le courent _5V_ entre par une des connextion (pattes), passe par le module puis ressort vers la _GND_
2. Lors du passage du _5V_ dans le modules, le courent est deviée pour entre envoyée sur la/les pattes correspondante au module
3. La carte principale va lire les trois pattes et en fonction de leurs signal (_5V_ = High | _0V_ = LOW) la carte identifie le(s) module(s)
4. Apres avoir identifiée les different modules connectée, la carte va appliquée les bons calcul pour obtenir des valeurs utilisable