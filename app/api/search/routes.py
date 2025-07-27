from flask import Blueprint, request, jsonify
from app.api.search.controllers import SearchController

search_bp = Blueprint('search', __name__, url_prefix='/v1')


@search_bp.route('/pokemon', methods=['GET'])
def search_pokemon():
    name = request.args.get('nombre')
    type = request.args.get('tipo')

    results = SearchController.search_pokemon(name=name, type=type)
    return jsonify([result.dict() for result in results])