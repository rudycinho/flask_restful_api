from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate,identify
from resources.user import UserRegister
from resources.item import Item,ItemList

from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='mark'
api = Api(app)

@app.before_first_request
def create_table():
    db.create_all()

jwt = JWT(app,authenticate,identify)

api.add_resource(Item,'/items/<string:name>')
api.add_resource(ItemList,'/items/')
api.add_resource(UserRegister,'/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000,debug=True)