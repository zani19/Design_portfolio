from flask import Flask, render_template, redirect, request
""" from flask_mail import Mail, Message
from config import email, senha """

app = Flask(__name__)
""" app;secret_key = 'zani19' """

""" mail_settings = {
    "MAIL_SERVER":'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": email,
    "MAIL_PASSWORD": senha
} """

""" app.config.update(mail_settings)
mail = Mail(app) """

""" class Contato:
    def __init__ (self, nome, email, mensagem):
        self.nome = nome,
        self.email = email,
        self.mensagem = mensagem """

@app.route('/')
def index():
    return render_template('/public/index.html')

""" @app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form["nome"], 
            request.form["email"],
            request.form["mensagem"]
        )

        msg = Message(
            subject = 'Contato do Portfólio'
        ) """

@app.route('/sobre')
def sobre():
    return render_template('/public/sobre.html')

@app.route('/projetos')
def projetos():
    return render_template('/public/projetos.html')

@app.route('/contato')
def contato():
    return render_template('/public/contato.html')

if __name__ == '__main__':
    app.run(debug=True)