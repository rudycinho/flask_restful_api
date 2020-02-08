from flask import Flask,request
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate,identify
from resources.user import UserRegister
from resources.item import Item,ItemList

app = Flask(__name__)
app.secret_key='mark'
api = Api(app)

jwt = JWT(app,authenticate,identify)

api.add_resource(Item,'/items/<string:name>')
api.add_resource(ItemList,'/items/')
api.add_resource(UserRegister,'/register')

if __name__ == '__main__':
    app.run(port=5000,debug=True)