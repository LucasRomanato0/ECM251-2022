from datetime import date
from select import select

class Document:
       def __init__(self, authors = [], date = date.today()) -> None:
              self._authors = authors  #_ torna privado
              self._date = date
       def __str__(self) -> str:
              return f'Document: \n\tAuthors: {self._authors} \n\tDate: {self._date}'
       def get_authors(self):
              return self._authors
       def get_date(self):
              return self._date
       def add_authors(self, author):
              self._authors.append(author)

class Email(Document): #Herança
       def __init__(self, to, subject = "No Subject", authors=[], date=date.today()) -> None:
              super().__init__(authors, date)
              self._subject = subject
              self._to = to
       def get_subject(self):
              return self._subject
       def get_to(self):
              return self._to

       def __str__(self) -> str:
              return f'Email: \n\tto: {self._to} \n\tsubject: {self._subject} \n\tauthors: {super().get_authors()} \n\tdate: {super().get_date()}'

class Book(Document): #Herança
       def __init__(self, title, authors=[], date=date.today()) -> None: #herdou de Document
              super().__init__(authors, date) #super() invoca a classe pai
              self._title = title
       def get_title(self):
              return self._title
       def __str__(self) -> str:
              return f'Book: \n\tTitle: {self._title} \n{super().__str__()}'
