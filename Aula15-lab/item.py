class Item():
    def __init__(self, preco, nome, descricao=None): #contrutor em python
        self._preco = preco
        self._nome = nome
        self._descricao = descricao

    def get_nome(self): #getter em python
        return self._nome

    def get_preco(self):
        return self._preco
    
    def get_descricao(self):
        return self._descricao

    def __str__(self) -> str: #toString em python
        return f'Nome:{self._nome}\nPreço: R${self._preco}'

    def __eq__(self, __o: object) -> bool: #comparação
        if isinstance(__o, Item):
            return self._nome == __o.get_nome()
        return False