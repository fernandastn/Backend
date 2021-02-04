from ..extensions import db
from ..association import association_table

#criando atributos da classe materia
class Materia(db.model)
    __tablename__ = 'materia'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.string(50), nullable=False)
    codigo = db.Column(db.string(30), nullable=False)


    #relacionando tabelas
    boletim = db.relationship('Boletim', backref='materia')
    turma = db.relationship('Turma', backref='materia')

    