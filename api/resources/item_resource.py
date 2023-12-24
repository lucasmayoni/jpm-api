from flask import Blueprint, jsonify, request, abort

from api.models.category import Category
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


@item_api.route('/items/search', methods=['GET'])
def filter_by_category_or_provider():
    if not request.json or not 'categoria_id' in request.json or not 'proveedor_id' in request.json:
        abort(400)
    items = []
    results = Item.filter_by_category_or_provider(request.json['categoria_id'], request.json['proveedor_id'])
    if results:
        for res in results:
            items.append(res.serialize())
        return items
    else:
        return {'message': 'No items found'}, 404


@item_api.route('/items/', methods=['POST'])
def create():
    if not request.json or not 'articulo_descripcion' in request.json:
        abort(400)
    data = request.get_json()
    item = Item(data['articulo_cod03'], data['articulo_descripcion'], data['articulo_precio'], data['articulo_proveedor'])
    item.save()
    return jsonify({'item': item.serialize()}), 201

