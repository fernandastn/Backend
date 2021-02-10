from flask import request, Blueprint, jsonify
from app.cardapio.model import Cardapio
from app.extensions import db

cardapio_api = Blueprint("cardapio_api", __name__)
@cardapio_api.route('/Cardapio', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        cardapio = Cardapio.query.all()
        return jsonify([cardapio.json() for cardapio in cardapio]), 200

    if request.method == 'POST':
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

@cardapio_api.route('/Cardapio/<int:id', methods = ['GET', 'PUT', 'POST', 'DELETE'])
def pagina_cardapio(id):
    cardapio = Cardapio.query.get_or_404(id)

    if request.method == 'GET':
        return cardapio.json(), 200

    if request. method == 'PATCH':
        dados = request.json

        bebidas = dados.get('bebidas', cardapio.bebidas)
        snacks = dados.get('snacks', cardapio.snacks)
        doces = dados.get('doces', cardapio.doces)

        if not isinstance(bebidas, str) or not isinstance(snacks, str) or not isinstance(doces, str):
            return{'ERRO!': 'tipo errado'}, 400
            
        db.session.commit()

        return cardapio.json(), 200
        











    
    