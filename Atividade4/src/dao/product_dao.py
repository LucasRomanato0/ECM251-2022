import sqlite3
from src.modules.product import Product

class ProductDAO:
       _instance = None

       def __init__(self) -> None:
              self.connect()

       @classmethod
       def get_instance(cls):
              if cls._instance == None:
                     cls._instance = ProductDAO()
              return cls._instance
       def _connect(self):
              self.conn = sqlite3.connect('./databases/sqlite_final.db', check_same_thread=False)
              print('Conectou')

       #CRUD
       #Create
       def create_product(self, product):
              try:
                     self.cursor = self.conn.cursor()
                     self.cursor.execute(f"""
                            INSERT INTO Product (cd, name, category, description, image, price)
                            VALUES('{product.id}', '{product.name}', '{product.category}', '{product.description}', '{product.image}', {product.price});
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
                     SELECT * FROM Product;
              """)
              resultados = []
              for resultado in self.cursor.fetchall():
                     resultados.append(Product(cd=resultado[0], name=resultado[1], category=resultado[2], description=resultado[3], image=resultado[4], price=resultado[5]))
              self.cursor.close()
              return resultados

       def get_product(self, cd):
              self.cursor = self.conn.cursor()
              self.cursor.execute(f"""
                     SELECT * FROM Product
                     WHERE cd = '{cd}';
              """)
              product = None
              resultado = self.cursor.fetchone()
              if resultado != None:
                     product = Product(cd=resultado[0], name=resultado[1], category=resultado[2], description=resultado[3], image=resultado[4], price=resultado[5])
              self.cursor.close()
              return product

       #Update
       def update_product(self, product):
              try:
                     self.cursor = self.conn.cursor()
                     self.cursor.execute(f"""
                            UPDATE Product SET
                            name = '{product.name}',
                            category = '{product.category}',
                            description = '{product.description}',
                            image = '{product.image}',
                            price = {product.price},
                            WHERE cd = {product.cd}
                     """)
                     self.conn.commit()
                     self.cursor.close()
              except:
                     return False
              return True

       #Delete
       def delete_product(self, cd):
              try:
                     self.cursor = self.conn.cursor()
                     self.cursor.execute(f"""
                            DELETE FROM Product 
                            WHERE cd = '{cd}'
                     """)
                     self.conn.commit()
                     self.cursor.close()
              except:
                     return False
              return True
