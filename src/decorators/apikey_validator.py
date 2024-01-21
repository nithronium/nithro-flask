from functools import wraps
from flask import request, jsonify
from src.api.responses import error_response
import hmac
import hashlib
from flask import request

from src.modules.apps.models import Apps


def validate_hmac_signature(secret_key, request, received_signature):
    # Create a message from the request data. You might need to adjust how you create this message based on your request structure.
    message = request.data

    # Create a HMAC signature
    hmac_signature = hmac.new(secret_key.encode(), message, hashlib.sha256).hexdigest()

    # Compare the computed signature with the received signature
    return hmac.compare_digest(hmac_signature, received_signature)


def apikey_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        public_key = request.headers.get("X-API-KEY")
        signature = request.headers.get("X-Signature")

        if not public_key or not signature:
            return error_response("Missing API key or signature", 401)

        app = Apps.query.filter_by(public_key=public_key).first()
        if not app:
            return error_response("Invalid API key", 401)

        # Assuming 'app.api_secret' is the shared secret key for HMAC
        valid_signature = validate_hmac_signature(app.private_key, request, signature)

        if not valid_signature:
            return error_response("Invalid signature", 401)

        return f(*args, **kwargs)

    return decorated_function
