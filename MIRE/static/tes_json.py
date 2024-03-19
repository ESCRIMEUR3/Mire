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
            print("bienvenue")
        else:
            print("mot de passe incorrect")
        break
if not trouvé:
    print("ce mail n'est pas enregistré") 
