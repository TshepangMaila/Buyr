from flask_restful import Resource, reqparse
from controllers.UserController import UserController


login_parse = reqparse.RequestParser()

login_parse.add_argument('email', type=str, required=True, help="Missing an Email Field")
login_parse.add_argument('password', type=str, required=True, help="Missing a Password Field")


register_parse = reqparse.RequestParser()

register_parse.add_argument('username', type=str, required=True, help="Missing a Username Field")
register_parse.add_argument('email', type=str, required=True, help="Missing an Email Field")
register_parse.add_argument('password', type=str, required=True, help="Missing a Password Field")


class LoginResource(Resource):

    def post(self):

        data = login_parse.parse_args()

        return UserController.login(email=data['email'], password=data['password'])


class RegisterResource(Resource):

    def post(self):

        data = register_parse.parse_args()

        return UserController.register(email=data['email'], username=data['username'], password=data['password'])

