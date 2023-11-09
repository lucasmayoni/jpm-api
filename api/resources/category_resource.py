from flasgger import swag_from
from flask import Blueprint, jsonify

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
