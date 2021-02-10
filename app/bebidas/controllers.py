from flask import request, Blueprint, jsonify
from .model import Bebidas
from app.extensions import db

#Bebidas
bebidas_api = Blueprint("bebidas_api", __name__)
@bebidas_api.route('/Bebidas', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        bebidas = Bebidas.query.all()
        return jsonify([bebidas.json() for bebidas in bebidas]), 200

    if request.method == 'POST':
        dados = request.json

        sucos = dados.get('sucos')
        refrigerantes = dados.get('refrigerantes')
        cervejas = dados.get('cervejas')
        drinks = dados.get('drinks')
        energeticos = dados.get('energeticos')
        agua = dados.get('agua')

    if not isinstance (sucos, str) or not isinstance (refrigerantes, str) or not isinstance (cervejas, str) or not isinstance(drinks, str) or not isinstance(agua, str):
        return{'ERRO': 'selecione uma opção'}, 400

   
    bebidas = Bebidas (sucos = sucos, refrigerantes = refrigerantes, cervejas = cervejas, drinks = drinks, energeticos = energeticos, agua = agua)
    #DB
    db.session.add(bebidas)
    db.session.commit()

    return bebidas.json(), 200

#Caso o cliente queira fazer alterações na bebidas (adicionar/deletar).

@bebidas_api.route('/bebidas/<int:id', methods = ['GET', 'PUT', 'POST', 'DELETE'])
def pagina_bebidas(id):
    bebidas = Bebidas.query.get_or_404(id)

    if request.method == 'GET':
        return bebidas.json(), 200

    if request. method == 'PATCH':
        dados = request.json

        sucos = dados.get('sucos', bebidas.sucos)
        refrigerantes = dados.get('refrigerantes', bebidas.refrigerantes)
        cervejas = dados.get('cervejas', bebidas.cervejas)
        drinks = dados.get('drinks', bebidas.drinks)
        energeticos = dados.get('energeticos', bebidas.energeticos)
        agua = dados.get('agua', bebidas.agua)


        if not isinstance(sucos, str) or not isinstance(refrigerantes, str) or not isinstance(cervejas, str) or not isinstance(drinks, str) or not isinstance(energeticos, str) or not isinstance(agua, str):
            return{'ERRO!': 'tipo errado'}, 400
            
        db.session.commit()

        return bebidas.json(), 200
        