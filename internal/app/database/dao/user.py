from sqlalchemy.orm import Session

from internal.app.database.models import User


class UserDAO:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return self.session.query(User).all()

    def get_one(self, uid):
        return self.session.query(User).filter_by(id=uid).first()

    def get_by_username(self, username):
        return self.session.query(User).filter_by(username=username).first()

    def get_by_email(self, email):
        return self.session.query(User).filter_by(email=email).first()

    def create(self, data):
        user = User(**data)
        self.session.add(user)
        self.session.commit()

    def update(self, uid, data):
        user = self.get_one(uid)
        if "username" in data:
            user.username = data.get("username")
        if "email" in data:
            user.email = data.get("email")
        if "password" in data:
            user.password = data.get("password")
        user.save()
        self.session.commit()

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()
