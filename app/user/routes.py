from flask import Blueprint
from .controllers import  (User_Login, Pagina_User)

user_api.add_url_rule(
    '/user/', view_func=User_Login.as_view('user_login'), method=['POST'])


user_api.add_url_rule(
    '/user/<int:id>', view_func=Pagina_User.as_view('pagina_user'), method=['GET', 'PATCH']
)