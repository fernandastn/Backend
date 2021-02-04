from ..extensions import db
from ..association import association_table

class Boletim(db.model):
     __tablename__ = 'boletim'
     id = db.Column(db.Integer, primary_key=True)
     notas = db.Column(db.Integer, primary_key=True)
     aluno_id = db.Column(db.Interger, db.Foreignkey('aluno_id'))
     
     #relacionando as tabelas
     aluno = db.relationship('Aluno', backref='boletim')
     materia = db.relationship('Materia', backref='boletim')

