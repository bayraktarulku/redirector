from flask import Blueprint, request
from flask_restful import Api, Resource
from app.controllers.redirection import (create_redirection,
    update_redirection, get_redirection_value, delete_redirection,)
from app.api.data_schemas import REDIRECTION_SCHEMA
from schema import SchemaError

bp = Blueprint(__name__, 'redirection_api')

api = Api(bp)


class Redirection(Resource):
    def get(self):

        redirect = get_redirection_value(redirection_hash)
        if not redirect:
            abort(401)
        return {'status': 'OK',
                'records': redirect}

    def post(self):
        owner_id = request.args.get('id', None)
        try:
            data = REDIRECTION_SCHEMA.validate(request.json)
        except SchemaError:
            return {'status': 'error'}

        user = create_redirection(owner_id, data['url'])
        return {'status': 'OK'}

    def put(self):
        pass

    def delete(self):
        pass

api.add_resource(Redirection, '/redirect')
