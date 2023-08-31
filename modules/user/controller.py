from modules.user.model import UserModel, User
from db import session


class UserController:

    @staticmethod
    def create(user: UserModel):
        print(user)
        new_user = User(
            name=user.name,
            lastname=user.lastname,
            role=user.role,
            password=user.password,
            code=f'{user.role.value}{user.code}'
        )
        session.add_all([new_user])
        session.commit()
