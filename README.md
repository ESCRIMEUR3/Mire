# projet_m-t-o
# le projet méteo est un projet visant à fabriquer une météo modulable et pour toute conditions  

# Système d'identification des modules

J'utilise le même principe que pour le **Multiplexer** et le **demultiplexer**, pour faire simple :

1. Le courent _5V_ entre par une des connexions (pattes), passe par le module puis ressort vers la _GND_
2. Lors du passage du _5V_ dans le module, le courent est devié pour envoyer sur la/les pattes correspondantes au module
3. La carte principale va lire les trois pattes et en fonction de leurs signaux (_5V_ = High | _0V_ = LOW) la carte identifie le(s) module(s)
4. Apres avoir identifiés les differents modules connectés, la carte va appliquée les bons calculs pour obtenir des valeurs utilisables.
