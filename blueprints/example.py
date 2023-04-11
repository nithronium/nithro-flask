from flask import Blueprint, jsonify

example_bp = Blueprint('example_bp', __name__)

@example_bp.route('/example', methods=['GET'])
def example():
    return jsonify({'message': 'Hello, World!'}), 200