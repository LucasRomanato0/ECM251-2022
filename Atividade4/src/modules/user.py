class User():
       def __init__(self, name, username, email, password, cartao, credit) -> None:
              self.name = name
              self.username = username
              self.email = email
              self.password = password
              self.cartao = cartao
              self.credit = credit

       def __str__(self) -> str:
              return f'User(\nname:{self.name} \nusername:{self.username} \nemail:{self.email} \npassword:{self.password} \ncard:{self.cartao} \ncredit:{self.credit}\n)'