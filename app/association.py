from ..extension import db
#manytomany
association_table = db.Table('association', db.Model.metadata,
                            db.Column('cardapio', db.Interger, db.ForeignKey('cardapio.id'))
                            db.Column('bebidas',db.Interger, db.ForeignKey('bebidas.id')))