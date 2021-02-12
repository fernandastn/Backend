from flask import request, jsonify, render_template
from flask.views import MethodView
import bcrypt
from flask_mail import Message
from flask_jwt_extended import create_acess_token, jwt_required, get_jwt_identify

from app.cardapio.model import Cardapio


class CardapioDetails(MethodView):
    def get(self):
        cardapio = Cardapio.query.all()
        return jsonify([cardapio.json() for cardapio in cardapio]), 200

    def post(self):
        dados = request.json

        bebidas = dados.get('bebidas')
        snacks = dados.get('snacks')
        doces = dados.get('doces')

    if not isinstance(bebidas, str) or not isinstance(snacks, str) or not isinstance(doces, str):
        return{'ERRO': 'selecione uma opção'}, 400

    cardapio = Cardapio (bebidas = bebidas, snacks = snacks, doces = doces)
    #DB
    db.session.add(cardapio)
    db.session.commit()

    return cardapio.json(), 200

    #Caso o cliente queira fazer alterações no cardapio

# @cardapio_api.route('/Cardapio/<int:id', methods = ['GET', 'PUT', 'POST', 'DELETE'])

class Pagina_Cardapio(MethodView):

    def get(self, id):
        cardapio = Cardapio.query.get_or_404(id)
        return cardapio.json(), 200

    def patch(self, id):
        cardapio = Cardapio.query_or_404(id)
        dados = request.json

        bebidas = dados.get('bebidas', cardapio.bebidas)
        snacks = dados.get('snacks', cardapio.snacks)
        doces = dados.get('doces', cardapio.doces)

        if not isinstance(bebidas, str) or not isinstance(snacks, str) or not isinstance(doces, str):
            return{'ERRO!': 'tipo errado'}, 400
            
        db.session.commit()

        # return cardapio.json(), 200


        

        











    
    