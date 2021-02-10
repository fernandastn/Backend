from .extensions import db
#manytomany
association_table = db.Table('association', db.Model.metadata,
                            db.Column('cardapio', db.Integer, db.ForeignKey('cardapio.id')),
                            db.Column('bebidas',db.Integer, db.ForeignKey('bebidas.id')))