from api import db
from api.models.item_category import ItemCategory


class Category(db.Model):
    __tablename__ = "categoria"
    categoria_id = db.Column(db.Integer, primary_key=True)
    categoria_descripcion = db.Column(db.String(100))
    categoria_estado = db.Column(db.Integer)
    items = db.relationship("ItemCategory",  back_populates="categoria")

    def __init__(self, categoria_descripcion, categoria_estado):
        self.categoria_descripcion = categoria_descripcion
        self.categoria_estado = categoria_estado

    def __repr__(self):
        return '<categoria_id {}>'.format(self.categoria_id)

    def serialize(self):
        return {
            'categoria_id': self.categoria_id,
            'categoria_descripcion': self.categoria_descripcion,
            'categoria_estado': self.categoria_estado
        }

    @staticmethod
    def get_categories_by_item_id(articulo_id):
        return db.session.query(Category).join(ItemCategory).filter(ItemCategory.articulo_id == articulo_id).all()

    @staticmethod
    def get_all():
        return db.session.query(Category).all()

    @staticmethod
    def get_by_id(categoria_id):
        return db.session.query(Category).filter_by(categoria_id=categoria_id).first()

    @staticmethod
    def search_by_description(categoria_descripcion):
        return (db.session.query(Category).
                filter(Category.categoria_descripcion.like('%' + categoria_descripcion + '%')).all())

    def save(self):
        db.session.add(self)
        db.session.commit()

