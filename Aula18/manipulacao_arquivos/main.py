#Programa que escreve em um arquivo

arquivo = open("dados.txt", "a")
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
