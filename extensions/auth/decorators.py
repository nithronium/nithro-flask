from functools import wraps
from flask import request, jsonify

def authorized_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header or auth_header != 'YOUR_TOKEN_HERE':
            return jsonify({'message': 'Unauthorized'}), 401
        return func(*args, **kwargs)
    return wrapper
