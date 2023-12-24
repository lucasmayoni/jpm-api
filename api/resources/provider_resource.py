from flask import Blueprint, jsonify, request, abort

from api.models.provider import Provider
from api.models.item import Item

provider_api = Blueprint('provider_api', __name__)


@provider_api.route('/providers', methods=['GET'])
def get_all():
    providers = []
    results = Provider.get_all()
    if results:
        for res in results:
            providers.append(res.serialize())
        return providers
    else:
        return {'message': 'No categories found'}, 404


@provider_api.route('/providers/', methods=['POST'])
def create():
    if not request.json or not 'proveedor_nombre' in request.json:
        abort(400)
    provider = Provider(request.json['proveedor_nombre'], request.json['proveedor_link'], request.json['proveedor_estado'])
    provider.save()
    return jsonify({'provider': provider.serialize()}), 201
