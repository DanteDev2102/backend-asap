from modules.user.model import UserModel, User, LoginModel
from db import session
from sqlalchemy import select


class UserController:

    @staticmethod
    def create(user: UserModel):
        new_user = User(
            name=user.name,
            lastname=user.lastname,
            role=user.role,
            password=user.password
        )

        session.add(new_user)
        session.commit()

        new_user.code = f"{user.role.value}{str(new_user.id).zfill(5)}"
        session.commit()
        session.refresh(new_user)

        return new_user

    # @staticmethod
    # def update(user_id:int, fields: dict):
    #     pass

    @staticmethod
    def unlink(code:str):
        user = session.query(User).filter_by(code=code).first()
        user.active = not user.active
        session.commit()
        session.refresh(user)
        return user

    @staticmethod
    def search_one(code:str):
        user = session.query(User).filter_by(code=code).first()
        return user

    @staticmethod
    def search():
        result = session.query(User)
        return result.all()

    @staticmethod
    def login(login:LoginModel):
        user = session.query(User).filter_by(code=code,active=True).first()

        if not user:
            return "wrong data"

        if user.password == login.password
            return user

        return "wrong data"
