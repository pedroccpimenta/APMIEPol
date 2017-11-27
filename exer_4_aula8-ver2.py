# Exemplo inserir (escrever) os dados de uma só vez (utilizando múltiplas linhas)

import csv

f = open('nomesIdade.csv', 'w', newline='') 
w = csv.writer(f) # o registo dos dados é feito no formato csv

novaLinha=[]
listaLinhas=[]
# cria uma lista com sublistas (exemplo listaLinhas = [[0, 'nome', 10], [1, 'n",nome', 11], [2, 'nome', 12]])

nome="a"
while  nome!="":
    nome=input("nome ")
    idade=input("idade ")
    novaLinha.append(nome)
    novaLinha.append(idade)
    print(novaLinha)
    listaLinhas.append(novaLinha)
    novaLinha=[]
    print(listaLinhas)

# escreve (grava) no ficheiro a lista e sublistas associadas de uma só vez
w.writerows(listaLinhas)
f.close()