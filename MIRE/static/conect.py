import json

with open('client.json', 'r') as f:
    data = json.load(f) #data est une liste de dictionnaires {"id_client: ....., "mail": ....., "mdp": .....}
mél = input("votre mail ?")
pwd = input("votre mot de passe ? ")
trouvé = False
for ligne in data:
    #print(ligne['mail'])
    if mél == ligne["mail"]:
        trouvé = True
        if pwd == ligne["pwd"]:
            print("Bienvenue")
        else:
            print("Mot de passe incorrect")
        break
if not trouvé:
    print("Ce mail n'est pas enregistré") 
