from src.modules.user import User
from src.dao.user_dao import UserDAO

class UserController():
       def __init__(self) -> None:
              pass

       def create_user(self, user) -> bool:
              try:
                     UserDAO.get_instance().create_user(user)
              except:
                     return False
              return True

       def get_all(self) -> list[User]:
              users = UserDAO.get_instance().get_all()
              return users

       def get_user(self, username) -> User:
              user = UserDAO.get_instance().get_user(username)
              return user

       def update_user(self, user) -> bool:
              return UserDAO.get_instance().update_user(user)

       def delete_user(self, user) -> bool:
              return UserDAO.get_instance().delete_user(user)