from ..extension import db
#manytomany
association_table = db.Table('association', db.Model.metadata,
                            db.Column('aluno', db.Interger, db.ForeignKey('aluno.id'))
                            db.Column('turma',db.Interger, db.ForeignKey('turma.id')))