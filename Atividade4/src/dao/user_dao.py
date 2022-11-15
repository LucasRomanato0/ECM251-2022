import sqlite3
from src.modules.user import User

class UserDAO:
       _instance = None

       def __init__(self) -> None:
              self.connect()

       @classmethod
       def get_instance(cls):
              if cls._instance == None:
                     cls._instance = UserDAO()
              return cls._instance
       def _connect(self):
              self.conn = sqlite3.connect('./databases/sqlite_final.db', check_same_thread=False)
              print('Conectou')

       #CRUD
       #Create
       def create_user(self, user):
              try:
                     self.cursor = self.conn.cursor()
                     self.cursor.execute(f"""
                            INSERT INTO User (name, username, email, password, cartao, credit)
                            VALUES('{user.name}', '{user.username}', '{user.email}', '{user.password}', '{user.cartao}', {user.credit});
                     """)
                     self.conn.commit()
                     self.cursor.close()
              except:
                     return False
              return True

       #Read
       def get_all(self):
              self.cursor = self.conn.cursor()
              self.cursor.execute("""
                     SELECT * FROM User;
              """)
              resultados = []
              for resultado in self.cursor.fetchall():
                     resultados.append(User(name=resultado[0], username=resultado[1], email=resultado[2], password=resultado[3], cartao=resultado[4], credit=resultado[5]))
              self.cursor.close()
              return resultados

       def get_user(self, username):
              self.cursor = self.conn.cursor()
              self.cursor.execute(f"""
                     SELECT * FROM User
                     WHERE username = '{username}';
              """)
              user = None
              resultado = self.cursor.fetchone()
              if resultado != None:
                     user = User(name=resultado[0], username=resultado[1], email=resultado[2], password=resultado[3], cartao=resultado[4], credit=resultado[5])
              self.cursor.close()
              return user

       #Update
       def update_user(self, user):
              try:
                     self.cursor = self.conn.cursor()
                     self.cursor.execute(f"""
                            UPDATE User SET
                            email = '{user.email}',
                            password = '{user.password}'
                            WHERE username = '{user.username}'
                     """)
                     self.conn.commit()
                     self.cursor.close()
              except:
                     return False
              return True

       #Delete
       def delete_user(self, username):
              try:
                     self.cursor = self.conn.cursor()
                     self.cursor.execute(f"""
                            DELETE FROM User 
                            WHERE username = '{username}'
                     """)
                     self.conn.commit()
                     self.cursor.close()
              except:
                     return False
              return True