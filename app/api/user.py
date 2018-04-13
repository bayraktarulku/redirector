from flask import Blueprint
from flask_restful import Api, Resource
bp = Blueprint(__name__, 'user_api')

api = Api(bp)


class User(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
