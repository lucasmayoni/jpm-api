from flask import Blueprint, jsonify, request, abort

from api.models.category import Category
from api.models.item import Item

category_api = Blueprint('category_api', __name__)


@category_api.route('/categories', methods=['GET'])
def get_all():
    categories = []
    results = Category.get_all()
    if results:
        for res in results:
            categories.append(res.serialize())
        return categories
    else:
        return {'message': 'No categories found'}, 404


@category_api.route('/categories/', methods=['POST'])
def create():
    if not request.json or not 'categoria_descripcion' in request.json:
        abort(400)
    category = Category(request.json['categoria_descripcion'], request.json['categoria_estado'])
    category.save()
    return jsonify({'category': category.serialize()}), 201
