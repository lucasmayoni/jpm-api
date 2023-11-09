from api import db


class Provider(db.Model):
    __tablename__ = 'proveedor'
    proveedor_id = db.Column(db.Integer, primary_key=True)
    proveedor_nombre = db.Column(db.String(70))
    proveedor_link = db.Column(db.String(250))
    proveedor_estado = db.Column(db.Integer)
    items = db.relationship('Item', back_populates='proveedor')

    def __init__(self, proveedor_nombre, proveedor_link, proveedor_estado):
        self.proveedor_nombre = proveedor_nombre
        self.proveedor_link = proveedor_link
        self.proveedor_estado = proveedor_estado

    def __repr__(self):
        return '<proveedor_id {}>'.format(self.proveedor_id)

    def serialize(self):
        return {
            'proveedor_id': self.proveedor_id,
            'proveedor_nombre': self.proveedor_nombre,
            'proveedor_link': self.proveedor_link,
            'proveedor_estado': self.proveedor_estado
        }

    @staticmethod
    def get_all():
        return db.session.query(Provider).all()

    @staticmethod
    def get_by_id(proveedor_id):
        return db.session.query(Provider).filter_by(proveedor_id=proveedor_id).first()

    @staticmethod
    def search_by_name(proveedor_nombre):
        return (db.session.query(Provider).
                filter(Provider.proveedor_nombre.like('%' + proveedor_nombre + '%')).all())

    def save(self):
        db.session.add(self)
        db.session.commit()

