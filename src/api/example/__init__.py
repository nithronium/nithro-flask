from flask import Blueprint

blueprint = Blueprint(
  'example_api_blueprint',
  __name__,
  url_prefix='/api/v1/example'
)