from flask import Flask
from dotenv import load_dotenv
import os
load_dotenv()

from db import db
from blueprints import get_blueprints

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

for blueprint in get_blueprints():
  app.register_blueprint(blueprint)
  
if __name__ == '__main__':
    app.run(debug=False, port=8000, host='0.0.0.0')
