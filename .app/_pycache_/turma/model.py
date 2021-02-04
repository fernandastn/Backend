from ..extensions import db
from ..association import association_table

#criando atributos da classe turma
class Turma(db.Model):
     __tablename__ = 'turma'
     id = db.Column(db.Integer, primary_key=True)
     horario = db.Column(db.string(30), nullable=False)

     #relacionando tabelas
     aluno = db.relationship('Aluno', secundary=association_table, backref='turma')
     professor = db.relationship('Professor', backref='turma')
     materia = db.relationship('Materia', backref='turma')

    