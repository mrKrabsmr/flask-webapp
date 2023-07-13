from internal.app.database.dao import user_dao, survey_dao, result_dao
from internal.app.services.registration import RegistrationService


class ProfileService:

    def get_profile_info(self, uid):
        user = user_dao.get_one(uid)
        return {
            "user": user,
            "total_surveys": self.get_total_surveys(uid),
            "total_results": self.get_total_results(uid),
        }

    @staticmethod
    def partial_update(uid, data):
        if "username" in data:
            if not RegistrationService.validate_username(data.get("username")):
                return False
        if "email" in data:
            if not RegistrationService.validate_email(data.get("data")):
                return False
        if "password" in data:
            if not RegistrationService.validate_password(data.get("password")):
                return False

        user_dao.update(uid, data)
        return True

    @staticmethod
    def all_user_surveys(uid):
        user = user_dao.get_one(uid)
        return user.surveys

    @staticmethod
    def get_total_surveys(uid):
        return survey_dao.get_().filter_by(user_id=uid).count()

    @staticmethod
    def get_total_results(uid):
        return result_dao.get_().filter_by(user_id=uid).count()
