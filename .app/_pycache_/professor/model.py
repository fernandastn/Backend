from ..extensions import db
from ..association import association_table

#criando atributos da classe professor
class Professor(db.Model):
    __tablename__ = 'professor'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.string(50), nullable=False)
    cpf = db.Column(db.string(50), nullable=False)
    formação = db.Column(db.string(50), nullable=False)


    #relacionando tabelas 
    turma = db.relationship('Turma', backref='professor')
