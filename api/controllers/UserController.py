from models.user import User
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token)

class UserController:

    @staticmethod
    def login(email: str, password: str) -> dict:

        user = User.find_by_email(email)

        if user and safe_str_cmp(user.password, password):

            return {
                "access_token" : create_access_token(identity=user.id, fresh=True),
                "refresh_token" : create_refresh_token(user.id)
            }
        
        return { "message" : "Invalid Credentials" }

    @staticmethod
    def register(email: str, username: str, password: str) -> dict:

        if User.find_by_email(email) or User.find_by_username(username):
            return {"message" : "This user already exists in the system"}

        user = User(email=email, username=username, password=password)
        user.save()