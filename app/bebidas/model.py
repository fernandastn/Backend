from ..extensions import db
from ..association import association_table

#criando atributos da classe materia
class Bebidas(db.Model):
    __tablename__ = 'bebidas'
    id = db.Column(db.Integer, primary_key=True)

    sucos = db.Column(db.String(30), nullable=False)
    refrigerantes = db.Column(db.String(30), nullable=False)
    cervejas = db.Column(db.String(30), nullable=False)
    drinks = db.Column(db.String(30), nullable=False)
    energeticos = db.Column(db.String(30), nullable=False)
    agua = db.Column(db.String(30), nullable=False)
    cardapio_id = db.Column(db.Integer, db.ForeignKey('cardapio.id'))


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
    sucos = db.relationship('Sucos', secondary = association_table, backref='bebidas')
    cardapio = db.relationship('Cardapio', backref = 'bebidas')

    