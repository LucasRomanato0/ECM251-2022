from src.models.pedido import Pedido
from src.models.item import Item

pedido1 = Pedido(1, "ABC", 10, "lskfdj", "teste", "19/10/2022-9:18")
pedido2 = Pedido(2, "SQL", 2, "lskfdj", "teste", "19/10/2022-9:18")

item1 = Item("SQL", "Aula", 19.90)
item2 = Item("LALAL", "Música", 12.90)

print(pedido1)
print(pedido2)

print(item1)
print(item2)