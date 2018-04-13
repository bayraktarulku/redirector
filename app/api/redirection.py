from flask import Blueprint, request
from flask_restful import Api, Resource
bp = Blueprint(__name__, 'redirection_api')

api = Api(bp)


class Redirection(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

api.add_resource(Redirection, '/redirect')
