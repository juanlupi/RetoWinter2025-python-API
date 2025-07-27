from flask import Blueprint, request, jsonify
from app.api.horoscope.controllers import HoroscopeController
from app.api.horoscope.schemas import HoroscopeRequest
from pydantic import ValidationError

# Create a Blueprint for horoscope routes
horoscope_bp = Blueprint('horoscope', __name__, url_prefix='/v1')


@horoscope_bp.route('/horoscope', methods=['POST'])
def get_horoscope():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Validate request data using Pydantic schema
        horoscope_request = HoroscopeRequest(
            name=data.get('name'),
            fecha_nacimiento=data.get('fecha_nacimiento')
        )

        # Process the request through controller
        response = HoroscopeController.get_horoscope(horoscope_request)

        # Return the successful response
        return jsonify(response.dict()), 200

    except ValidationError as e:
        # Handle validation errors
        return jsonify({
            'error': 'Validation error',
            'details': e.errors()
        }), 400

    except Exception as e:
        # Handle other unexpected errors
        return jsonify({
            'error': 'Internal server error',
            'message': str(e)
        }), 500