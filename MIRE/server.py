from flask import Flask, render_template, request, session, redirect, url_for
import json
from os.path import join, dirname, realpath

app = Flask(__name__)

app.config['DATA_DIR'] = join(dirname(realpath(__file__)),'static')
app.secret_key = b'99b45274a4b2da7440ab249f17e718688b53b646f3dd57f23a9b29839161749f'

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/dashboard", methods=['POST'])
def dashboard():
    with open(url_for('static', filename='client.json'), 'r') as f:
        data = json.load(f) #data est une liste de dictionnaires {"id_client: ....., "mail": ....., "mdp": .....}
    mél = request.form['in_mail']
    pwd = request.form['mdp']
    trouvé = False
    for ligne in data:
        #print(ligne['mail'])
        if mél == ligne["mail"]:
            trouvé = True
            if pwd == ligne["pwd"]:
                res = "bienvenue"
            else:
                res = "mot de passe incorrect"
            break
    if not trouvé:
        res = "ce mail n'est pas enregistré"
    return render_template('dashboard.html', msg=res)

app.run(host = '127.0.0.1', port='8080', debug=True)