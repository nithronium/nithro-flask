from src import db
from src.api.example import blueprint
from flask import request
from extensions.auth.decorators import *
from src.example.models import Example
from extensions.api.utils import check_fields



@blueprint.route('/create', methods=['POST'])
@authorized_only
def create():
  
  required_fields = ['username', 'password']
  
  status = check_fields(required_fields, request)
  if not status:
    return {'message': 'Missing required fields'}, 400
  
  username = request.json['username']
  password = request.json['password']
  
  example = Example(username=username, password=password)
  db.session.add(example)
  db.session.commit()
  
  return {'message': 'Example created successfully'}, 201
