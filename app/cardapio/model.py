from ..extensions import db
from ..association import association_table

#criando atributos da classe cardapio
class Cardapio(db.Model):
    __tablename__ = 'cardapio'
    id = db.Column(db.Integer, primary_key=True)
    bebidas = db.Column(db.string(100), nullable=False)
    snacks = db.Column(db.string(100), nullable=False)
    doces = db.Column(db.string(100), nullable=False)

    def json(self):
        return{
            "bebidas": self.bebidas,
            "snacks": self.snacks,
            "doces": self.doces,
        }

    #Relacionando tabelas
    bebidas = db.relationship('Bebidas', backref='cardapio')
    




