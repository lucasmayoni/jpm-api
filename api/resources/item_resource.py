from flasgger import swag_from
from flask import Blueprint, jsonify
from api.models.item import Item

item_api = Blueprint('item_api', __name__)


@item_api.route('/items', methods=['GET'])
def get_all():
    items = []
    results = Item.get_all()
    if results:
        for res in results:
            items.append(res.serialize())
        return items
    else:
        return {'message': 'No items found'}, 404


@item_api.route('/items/<int:articulo_id>', methods=['GET'])
def get_by_id(articulo_id):
    item = Item.get_by_id(articulo_id)
    if item:
        return item.serialize()
    else:
        return {'message': 'Item not found'}, 404
