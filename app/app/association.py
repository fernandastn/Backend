from ..extension import db
#manytomany
association_table = db.Table('association', db.Model.metadata,
                            db.Column('Cardapio', db.Integer, db.ForeignKey('cardapio.id')),
                            db.Column('Bebidas', db.Integer, db.ForeignKey('bebidas.id')))