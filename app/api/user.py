from flask import Blueprint, request
from flask_restful import Api, Resource
bp = Blueprint(__name__, 'user_api')
from app.controllers.user import (create_user, change_password, del_user,
                                  get_redirections)
from app.api.data_schemas import USER_SCHEMA, UPDATE_USER_SCHEMA
from schema import SchemaError
api = Api(bp)


class User(Resource):

    def get(self):
        user_id = request.args.get('id', None)

        if not user_id:
            return {'status': 'error'}

        redirections = get_redirections(user_id)
        return {'status': 'OK',
                'redirections': redirections}

    def post(self):
            try:
                data = USER_SCHEMA.validate(request.json)
            except SchemaError as e:
                return {'status': 'error'}
            user = create_user(**data)

            return {'status': 'OK'}


    def put(self):
        try:
            data = UPDATE_USER_SCHEMA.validate(request.json)
        except SchemaError as e:
            return {'status': 'error',
                    'message': 'Missing or incorrect parameters'}

        if data['password'] == '':
            return {'status': 'error'}

        data['new_password'] = data[
            'new_password'] if 'new_password' in data else ''

        user = change_password(**data)

        return {'status': 'OK',
                'user': user}

    def delete(self):
        try:
            data = USER_SCHEMA.validate(request.json)
        except SchemaError as e:
            return {'status': 'error',
                    'message': 'Missing or incorrect parameters'}

        user = del_user(**data)
        return {'status': 'OK'}

api.add_resource(User, '/api/user')
