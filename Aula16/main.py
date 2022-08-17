from pydoc import doc
from modelos.documentos import Book, Document, Email
from modelos.plantas import Alface, Arvore

def run_system():
       doc1 = Document()
       doc2 = Email(to = '20.00313-7@maua.br',authors=['Lucas Romanato'])
       doc3 = Book(title = "Design Patterns", authors=['Erich Gamma', 'John Vlissides', 'Ralph Johnson', 'Richard Helm'])
       print(doc2)
       print(doc3)

if __name__ == "__main__":
       # planta1 = Arvore('Carvalho')
       # planta2 = Alface(nome='Hamburguer de Siri do Futuro')

       # print(planta1.ola())
       # print(planta2.ola())
       run_system()
