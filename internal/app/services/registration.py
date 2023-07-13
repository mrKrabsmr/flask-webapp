import hashlib
import os
import re

from flask import session

from internal.app.database.dao import user_dao


class RegistrationService:

    def create_user(self, data):
        if not self._validate_data(data):
            return False
        password = self.convert_password(data["password"])
        validated_data = {
            "username": data["username"],
            "email": data["email"],
            "password": password
        }
        user_dao.create(validated_data)
        self.create_session(validated_data)
        return True

    def _validate_data(self, data):
        if not self.validate_username(data.get("username")):
            return False
        if not self.validate_email(data.get("email")):
            return False
        if not self.validate_password(data.get("password")):
            return False
        return True

    @staticmethod
    def validate_username(username):
        username_pattern = re.compile(r'^[a-z0-9]{5,15}$')
        if not re.match(username_pattern, username):
            return False
        return True

    @staticmethod
    def validate_email(email):
        email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        if not re.match(email_pattern, email):
            return False
        return True

    @staticmethod
    def validate_password(password):
        password_pattern = re.compile(r'^(?=.*\d).{8,}$')
        if not re.match(password_pattern, password):
            return False
        return True

    @staticmethod
    def create_session(data):
        user = user_dao.get_by_username(data["username"])
        session["user_id"] = user.id

    @staticmethod
    def convert_password(password, salt=os.urandom(32)):
        key = hashlib.pbkdf2_hmac(
            "sha256", password.encode("utf-8"), salt, int(os.getenv("NUMBER_OF_ITERATIONS"))
        )
        hashed_password = (salt + key).hex()
        return hashed_password

