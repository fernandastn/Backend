from ..extensions import db
from ..association import association_table

#criando atributos da classe aluno
class Aluno(db.Model):
    __tablename__ = 'aluno'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.string(20), nullable=False)
    cpf = db.Column(db.string(20), nullable=False)
    data_nascimento= db.Column(db.string(20), nullable=False)
    sexo = db.Column(db.string(20), nullable=False)
    periodo_ingresso = db.Column(db.string(20), nullable=False)
    curso = db.Column(db.string(20), nullable=False)
    boletim_id = db.Column(db.Integer, primary_key=True)

    #Relacionando tabelas
    boletim = db.relationship('Boletim', backref='aluno')
    turma = db.relationship('Turma', secundary=association_table, backref='aluno')




