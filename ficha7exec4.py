"""
Ficha 7

4. Fazer um programa que crie um ficheiro com uma lista de nomes e idades.
Oprograma deverá ir perguntado ao utilizador o nome e a idade e gravar os dadosnuma lista.
Se o nome for deixado em branco o programa não pede mais nomes egrava para um
ficheiro a(s) lista(s) com os dados respetivos.

"""
import csv

f = open('nomesIdade.csv', 'w', newline='') 
w = csv.writer(f) # o registo dos dados é feito no formato csv

lista=[]

nome = input (" nome ?")
while  nome!="":
    idade=input("idade ")
    lista.append([nome, idade]) #acrescenta à lista, uma lista com 2 elementos, nome e idade
    nome = input (" nome ?")

# escreve no ficheiro a lista
w.writerows(lista)
f.close()
