from flask import Blueprint
from .controllers import (SucosDetails, Pagina_sucos)


sucos_api = Blueprint('sucos_api', __name__)

sucos_api.add_url_rule(
    '/sucos', view_func=SucosDetails.as_views('sucosdetails'), methods=['GET', 'POST'])

cardapio_api.add_url_rule(
    '/sucos/<int:id>', view_func=Pagina_Sucos.as_view('pagina_sucos'), methods=['GET', 'PATCH'])