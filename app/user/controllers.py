from app.extensions import db, mail
from flask import request, jsonify, render_template
from flask.views import MethodView
import bcrypt
from flask_mail import Message
from flask_jwt_extended import create_acess_token, jwt_required, get_jwt_identify


class User_Login(MethodView):
    def get(self):
        user = User.query.all()
        return jsonify(user.json() for user in user), 200

    def post(self):
        dados = request.json

        nome = dados.get('nome')
        email = dados.get('email')
        password = str(dados.get('password'))

        if not isinstance(nome, str) or not isinstance(email, str) or not isinstance(password, str):
            return {'ERRO': "Tipo inválido"}, 400

        db.session.add(user)
        db.session.commit()


        password_hash = user(nome=nome, email=email, password=password)

        user = User_Login.query.filter_by(email=email).first()

        if not user or not bcrypt.checkpw(password.encode(), user.password_hash):
            return  {'ERRO': 'User não encontrado'}, 400

        token = create_token_acess_token(identify=user.id)


        msg = Menssage(sender = 'fernandasantana2304@gmail.com'
                       recipiente = [email],
                       subject = 'Bem-vindo a Lanchonete do Jamil!'
                       html = render_template('email.html', nome = nome))

        mail.send(msg)
        return user.json(), 200

class Pagina_User(MethodView):

   decorators = [jwt_required]
    
    def get(self, id):
        user = Pagina_User.query.get_or_404(id)
        return user.json(), 200

    def patch(self, id):
        user = Pagina_User.query_or_404(id)
        dados = request.json

        nome = dados.get('nome', user.nome)
        email = dados.get('email', user.email)
        password = dados.get('password', user.password)

        if not isinstance(nome, str) or not isinstance(email, str) or not isinstance(password, str):
            return{'ERRO!': 'tipo errado'}, 400

            
        db.session.commit()