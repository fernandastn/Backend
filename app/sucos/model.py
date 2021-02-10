from ..extensions import db
from ..association import association_table

#criando atributos da classe professor
class Sucos(db.Model):
    __tablename__ = 'sucos'
    id = db.Column(db.Integer, primary_key=True)
     detox = db.Column(db.string(30), nullable=False)
     abacaxi_com_hortela = db.Column(db.string(30), nullable=False)
     batata_doce = db.Column(db.string(30), nullable=False)
     laranja_com_cenoura = db.Column(db.string(30), nullable=False)
     manga = db.Column(db.string(30), nullable=False)
     proteico = db.Column(db.string(30), nullable=False)

     def json(self):
          return{
          "detox": self.detox,
          "abacaxi_com_hortelã": self.abacaxi_com_hortelã,
          "batata_doce": self.batata_doce,
          "laranja_com_cenoura": self.laranja_com_cenoura,
          "manga": self.manga,
          "proteíco": self.proteico
          }


    #relacionando tabelas 
    bebidas = db.relationship('Bebidas', backref='sucos')
