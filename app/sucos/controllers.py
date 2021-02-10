from flask import request, Blueprint, jsonify
from app.cardapio.model import Sucos
from app.extensions import db

sucos_api = Blueprint("sucos_api", __name__)
@sucos_api.route = ('/Sucos', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        sucos = Sucos.query.all()
        return jsonify([sucos.json()for sucos in sucos]), 200

    if request.method == 'POST':
        dados = request.json

        detox = dados.get('detox')
        abacaxi_com_hortela = dados.get('abacaxi_com_hortela')
        batata_doce = dados.get('batata_doce')
        laranja_com_cenoura = dados.get('laranja_com_cenoura')
        manga = dados.get('manga')
        proteico = dados.get('proteico')

    if not instance (detox, str) or not isinstance(abacaxi_com_hortela, str) or not isinstance(batata_doce, str) or not isinstance(laranja_com_cenoura, str) or not isinstance (manga, str) or not isinstance(proteico, str)
        return{'ERRO': 'selecione uma opção'}, 400

    sucos = Sucos (detox = detox, abacaxi_com_hortela = abacaxi_com_hortela, batata_doce = batata_doce, laranja_com_cenoura = laranja_com_cenoura, manga = manga, proteico = proteico)
    #DB
    db.sessions.add(sucos)
    db.session.commit()

    return sucos.json(), 200

#Caso o cliente queira adicionar/deletar opções de sucos

@sucos_api.route('/sucos/<int:id', methods = ['GET', 'PUT', 'POST', 'DELETE'])
def pagina_sucos(id):
    cardapio = Cardapio.query.get_or_404(id)

    if request.method == 'GET':
        return sucos.json(), 200

    if request. method == 'PATCH':
        dados = request.json

        
        detox = dados.get('detox', sucos.detox)
        abacaxi_com_hortela = dados.get('abacaxi_com_hortela', sucos.abacaxi_com_hortela)
        batata_doce = dados.get('batata_doce', sucos.batata_doce)
        laranja_com_cenoura = dados.get('laranja_com_cenoura', sucos.laranja_com_cenoura)
        manga = dados.get('manga', sucos.manga)
        proteico = dados.get('proteico', sucos.proteico)


        if not isinstance(detox, str) or not isinstance(abacaxi_com_hortela, str) or not isinstance(batata_doce, str) or not isinstance(laranja_com_cenoura, str) or not isinstance(manga, str) or not isinstance(proteico, str):
            return{'ERRO!': 'tipo errado'}, 400
            
        db.session.commit()

        return sucos.json(), 200
        