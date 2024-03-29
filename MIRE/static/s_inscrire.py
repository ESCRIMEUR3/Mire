import json

with open('client.json', 'r') as f:
    data = json.load(f) #data est une liste de dictionnaires {"id_client: ....., "mail": ....., "mdp": .....}