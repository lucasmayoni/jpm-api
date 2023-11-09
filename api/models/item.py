from sqlalchemy.orm import joinedload

from api import db
from api.models.item_category import ItemCategory
from api.models.provider import Provider
from api.models.category import Category


class Item(db.Model):
    __tablename__ = 'articulo'
    articulo_id = db.Column(db.Integer, primary_key=True)
    articulo_cod03 = db.Column(db.Integer)
    articulo_descripcion = db.Column(db.String(250))
    articulo_precio = db.Column(db.Float)
    articulo_proveedor = db.Column(db.Integer, db.ForeignKey('proveedor.proveedor_id'))
    proveedor = db.relationship('Provider', back_populates='items')
    categoria = db.relationship("Category", secondary=ItemCategory.__table__, back_populates="items")

    def __init__(self, articulo_cod03, articulo_descripcion, articulo_precio, articulo_proveedor):
        self.articulo_cod03 = articulo_cod03
        self.articulo_descripcion = articulo_descripcion
        self.articulo_precio = articulo_precio
        self.articulo_proveedor = articulo_proveedor

    def __repr__(self):
        return '<articulo_id {}>'.format(self.articulo_id)

    def serialize(self):
        return {
            'articulo_id': self.articulo_id,
            'articulo_cod03': self.articulo_cod03,
            'articulo_descripcion': self.articulo_descripcion,
            'articulo_precio': self.articulo_precio,
            'articulo_proveedor': self.proveedor.serialize() if self.proveedor is not None else '',
            'articulo_categoria': [cat.serialize() for cat in self.categoria] if self.categoria is not None else ''
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(articulo_id):
        return db.session.query(Item).filter_by(articulo_id=articulo_id).options(joinedload(Item.categoria)).first()

    @staticmethod
    def get_all():
        return db.session.query(Item).all()
