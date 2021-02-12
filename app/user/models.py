from ..extensions import db
from ..association import association_table

#criando atributos da classe cardapio
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)

    def json(self):
        return{
            "nome": self.nome,
            "email": self.email,
            "password": self.password,
        }

    #Relacionando tabelas
    bebidas = db.relationship('Bebidas', backref='cardapio')

