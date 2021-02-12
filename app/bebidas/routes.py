from flask import Blueprint
from .controllers import (BebidasDetails, Pagina_bebidas)


bebidas_api = Blueprint('bebidas_api', __name__)

bebidas_api.add_url_rule(
    '/bebidas', view_func=BebidasDetails.as_views('bebidasdetails'), methods=['GET', 'POST'])

bebidas_api.add_url_rule(
    '/bebidas/<int:id>', view_func=Pagina_Bebidas.as_view('pagina_bebidas'), methods=['GET', 'PATCH']