#Programa que escreve em um arquivo
try:
    arquivo = open("data/dados.txt", "a")
    continuar = True

    while continuar:
        #time é str
        time = input("Time (vazio para sair): ")
        #toda str vazia é falsa
        #entra no if se a str está vazia
        if not time:
            continuar = False
            continue
        arquivo.write(time+'\n')
    arquivo.close()

    x = 9+"ola"
except FileNotFoundError:
    print('Arquivo ou diretório não encontrado')
except ZeroDivisionError:
    print('Alguém tentou dividir por zero')
except:
    print('Algo de errado aconteceu!')
finally:
    print('Enfim terminou!')