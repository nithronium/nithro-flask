from flask import Blueprint

blueprint = Blueprint("logs_api_blueprint", __name__, url_prefix="/api/v1/logs")
