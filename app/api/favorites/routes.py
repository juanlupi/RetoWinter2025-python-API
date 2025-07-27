from flask import Blueprint, request, jsonify
from app.api.favorites.controllers import FavoritesController
from app.api.favorites.schemas import FavoriteCreate

favorites_bp = Blueprint('favorites', __name__, url_prefix='/v1')


@favorites_bp.route('/favorites', methods=['POST'])
def add_favorite():
    username = request.args.get('usuario')
    if not username:
        return jsonify({"error": "Username is required"}), 400

    data = request.get_json()
    try:
        favorite_data = FavoriteCreate(**data)
        result = FavoritesController.add_favorite(username, favorite_data.dict())
        return jsonify(result), 201  # No need for .dict() since it's already a dict
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@favorites_bp.route('/favorites', methods=['GET'])
def get_favorites():
    username = request.args.get('usuario')
    if not username:
        return jsonify({"error": "Username is required"}), 400

    favorites = FavoritesController.get_favorites(username)
    return jsonify(favorites), 200  # Directly return the list of dicts


@favorites_bp.route('/favorites/<int:favorite_id>', methods=['DELETE'])
def remove_favorite(favorite_id):
    username = request.args.get('usuario')
    if not username:
        return jsonify({"error": "Username is required"}), 400

    result = FavoritesController.remove_favorite(username, favorite_id)
    status = 200 if result['success'] else 404
    return jsonify(result), status  # Directly return the dict


@favorites_bp.route('/favoritos/<int:favorite_id>', methods=['GET'])
def get_favorite(favorite_id):
    username = request.args.get('usuario')
    if not username:
        return jsonify({"error": "El parámetro 'usuario' es requerido"}), 400

    favorite_data = FavoritesController.get_favorite_by_id(username, favorite_id)

    if not favorite_data:
        return jsonify({"message": "Favorito no encontrado"}), 404

    return jsonify(favorite_data), 200