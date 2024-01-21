from flask import jsonify


def error_response(message, status_code):
    return jsonify({"error": message}), status_code


def success_response(message, status_code):
    return jsonify({"success": message}), status_code
