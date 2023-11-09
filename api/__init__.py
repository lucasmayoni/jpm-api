from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:password@localhost/jpm"
db = SQLAlchemy(app)

from api.resources.item_resource import item_api
from api.resources.category_resource import category_api
# from app.resources.result_resource import result_api

app.register_blueprint(item_api)
app.register_blueprint(category_api)

swagger = Swagger(app)

with app.app_context():
    db.create_all()
