from flask import Blueprint
from .controllers import (CardapioDetails, Pagina_cardapio)


cardapio_api = Blueprint('cardapio_api', __name__)

cardapio_api.add_url_rule(
    '/cardapio', view_func=CardapioDetails.as_views('cardapiodetails'), methods=['GET', 'POST'])

cardapio_api.add_url_rule(
    '/cardapio/<int:id>', view_func=Pagina_Cardapio.as_view('pagina_cardapio'), methods=['GET', 'PATCH']

