from src.modules.product import Product
from src.dao.product_dao import ProductDAO

class ProductController():
       def __init__(self) -> None:
              pass

       def create_product(self, product) -> bool:
              try:
                     ProductDAO.get_instance().create_product(product)
              except:
                     return False
              return True

       def get_all(self) -> list[Product]:
              product = ProductDAO.get_instance().get_all()
              return product

       def get_product(self, cd) -> Product:
              product = ProductDAO.get_instance().get_product(cd)
              return product

       def update_product(self, product) -> bool:
              return ProductDAO.get_instance().update_user(product)

       def delete_product(self, cd) -> bool:
              return ProductDAO.get_instance().delete_user(cd)