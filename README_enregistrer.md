# Commuunication par Serial

Lee programmee et la carte Arduino va envoyer des données dans cette configuration : 
*[ID_Board]:[ID_Capteur]=[Val]*.
Le fichier 'enregistrer.py' va se charger  de recuperer les données envoyer, de les ecrires dans un fichiers du nom de *Board[ID_Board].txt* qui va recevoir uune seul ligne contenant les information précédante.
Suite a cela, le serveur va pouvoir avec un programme *lecteur*, lire les information du fichier *.txt*.