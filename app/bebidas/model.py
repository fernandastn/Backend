from ..extensions import db
from ..association import association_table

#criando atributos da classe materia
class Bebidas(db.model)
    __tablename__ = 'bebidas'
    id = db.Column(db.Integer, primary_key=True)

    sucos = db.Column(db.string(30), nullable=False)
    refrigerantes = db.Column(db.string(30), nullable=False)
    cervejas = db.Column(db.string(30), nullable=False)
    drinks = db.Column(db.string(30), nullable=False)
    energeticos = db.Column(db.string(30), nullable=False)
    agua = db.Column(db.string(30), nullable=False)
    cardapio_id = db.Column(db.integer, db.ForeingKey('cardapio.id'), pk = True)


    def json (self):
        return{
            "sucos": self.sucos,
            "refrigerantes": self.refrigerantes,
            "cervejas": self.cervejas,
            "drinks": self.drinks,
            "energeticos": self.energeticos,
            "agua": self.agua
        }


    #relacionando tabelas
    sucos = db.relationship('Sucos', secundary=association_table, backref='bebidas')
    cardapio = db.relationship('Cardapio', backref = 'bebidas')

    