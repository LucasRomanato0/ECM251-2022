class Product():
       def __init__(self, cd, name, category, description, image, price) -> None:
              self.cd = cd
              self.name = name
              self.category = category
              self.description = description
              self.image = image
              self.price = price

       def __str__(self) -> str:
              return f'Product(\ncd:{self.cd} \nname:{self.name} \ncategory:{self.category} \ndescription:{self.description} \nimage:{self.image} \nprice:{self.price}\n)'

       def get_name(self):
              return self._name
       def get_category(self):
              return self._category
       def get_description(self):
              return self._description
       def get_image(self):
              return self._image
       def get_price(self):
              return self._price
       