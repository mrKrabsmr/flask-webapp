from flask import session

from internal.app.database.dao import user_dao
from internal.app.services.registration import RegistrationService


class LoginService:
    def login_user(self, data):
        if not self._validate_data(data):
            return False
        RegistrationService.create_session(data)
        return True

    def _validate_data(self, data):
        login = data.get("login")
        password = data.get("password")
        if not login or not password:
            return False
        user = user_dao.get_by_username(login)
        if not user:
            user = user_dao.get_by_email(login)
            if not user:
                return False
        if not self.check_password(user.password, password):
            return False
        return True

    @staticmethod
    def check_password(valid_password, checking_password):
        salt = valid_password[:32]
        converted_password = RegistrationService.convert_password(
            checking_password, salt
        )
        return valid_password == converted_password
