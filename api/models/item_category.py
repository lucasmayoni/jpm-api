from api import db


class ItemCategory(db.Model):
    __tablename__ = "articulo_categoria"
    articulo_categoria_id = db.Column(db.Integer, primary_key=True)
    articulo_id = db.Column(db.Integer, db.ForeignKey('articulo.articulo_id'))
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.categoria_id'))
    categoria_orden = db.Column(db.Integer)

    items = db.relationship("Item", back_populates="categoria")
    categoria = db.relationship("Category", back_populates="items")

    def __init__(self, articulo_id, categoria_id, categoria_orden):
        self.articulo_id = articulo_id
        self.categoria_id = categoria_id
        self.categoria_orden = categoria_orden

    def __repr__(self):
        return '<articulo_categoria_id {}>'.format(self.articulo_categoria_id)

    def serialize(self):
        return {
            'articulo_categoria_id': self.articulo_categoria_id,
            'articulo_id': self.articulo_id,
            'categoria_id': self.categoria_id,
            'categoria_orden': self.categoria_orden
        }
