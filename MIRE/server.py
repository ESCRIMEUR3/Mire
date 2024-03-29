from flask import Flask, render_template, request, session, redirect, url_for
import json
from os.path import join, dirname, realpath

app = Flask(__name__)

app.config['DATA_DIR'] = join(dirname(realpath(__file__)),'static')
app.secret_key = b'99b45274a4b2da7440ab249f17e718688b53b646f3dd57f23a9b29839161749f'

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/connexion")
def connexion():
    truc = "Bienvenue sur l'interface de monitoring MIRE. Pour consulter les mesures de vos board, entrez vos indentifiants de connexion"
    return render_template('login.html', type="connexion", msg=truc)

@app.route("/inscription")
def inscription():
    truc = "Bienvenue sur l'interface de monitoring MIRE. Avant de consulter vos board, veuillez saisir les identifiants qui vous ont été communiqués pour finaliser la création de votre compte"
    return render_template('login.html', type="inscription", msg=truc)

@app.route("/coord")
def coord():
    if 'id_client' in session:
        session['chemin'] = 'rouge' # pour savoir comment on arrive sur la vue dashboard
    truc = "Bienvenue sur l'interface de monitoring MIRE. Si vous voulez acheter une board, veuillez remplir le formulaire ci dessous"
    if "id_client" in session:
        with open(join(app.config['DATA_DIR'],'coord.json'), 'r') as f:
            data = json.load(f) 
            #data est une liste de dictionnaires {"id_client: ....., "nom": ....., "prénom": ....., "tél": ....., "adresse": .....}
            for d in data:
                if d["id_client"] == session["id_client"]:
                    return render_template('coord.html', type="formulaire", msg=truc, data=d)
    else:
        session['chemin'] = 'vert'
        with open(join(app.config['DATA_DIR'],'coord.json'), 'a') as f:

            return render_template('coord.html', type="formulaire", msg=truc)


@app.route("/dashboard", methods=['POST'])
def dashboard():
    if 'chemin' in session and session['chemin']=='rouge':
        # creer un nouvel id_board x
        with open(join(app.config['DATA_DIR'],'boards.json'), 'r') as f:
            data = json.load(f) #data est une liste de dictionnaires {"id_board: ....., "id_client": .....}
        new_id = 0
        for ligne in data:
            if ligne["id_board"] > new_id:
                new_id = ligne["id_board"]
        new_id += 1
        # rajouter la ligne {"id_board": x, "id_client": session['id_client']} dans boards.json
        data.append({"id_board": new_id, "id_client": session['id_client']})
        with open(join(app.config['DATA_DIR'],'boards.json'), 'w') as f:
            json.dump(data, f) # nouvelle board associée au compte de id_client
        with open(join(app.config['DATA_DIR'],'boards.json'), 'r') as f:
            data = json.load(f) #data est une liste de dictionnaires {"id_board: ....., "id_client": .....}
        boards = []
        for ligne in data:
            if ligne["id_client"] == session["id_client"]:
                boards.append(ligne["id_board"])
        return render_template('dashboard.html', msg="", bs=boards)
    else:
        with open(join(app.config['DATA_DIR'],'client.json'), 'r') as f:
            data = json.load(f) #data est une liste de dictionnaires {"id_client: ....., "mail": ....., "mdp": .....}
        mél = request.form['in_mail']
        pwd = request.form['mdp']
        trouvé = False
        for ligne in data:
            #print(ligne['mail'])
            if mél == ligne["mail"]:
                trouvé = True
                if pwd == ligne["pwd"]:
                    res = "Bienvenue"
                    session['id_client'] = ligne["id_client"]
                else:
                    res = "Mot de passe incorrect"
                    return render_template('login.html',msg=res)
                break
        if not trouvé:
            res = "Ce mail n'est pas enregistré"
            return render_template('login.html',msg=res)
        #on construit la liste des id des boards associées à id_client
        with open(join(app.config['DATA_DIR'],'boards.json'), 'r') as f:
            data = json.load(f) #data est une liste de dictionnaires {"id_board: ....., "id_client": .....}
        boards = []
        for ligne in data:
            if ligne["id_client"] == session["id_client"]:
                boards.append(ligne["id_board"])
        return render_template('dashboard.html', msg=res, bs=boards)

@app.route("/deconnexion")
def deconnexion():
    session.pop('id_client')
    return render_template("adios.html")

app.run(host = '127.0.0.1', port='8080', debug=True)