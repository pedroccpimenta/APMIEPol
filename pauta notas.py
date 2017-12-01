import csv

lista=[]

print ('Estado inicial:')
l=open('pautanotas.csv', 'r') 
r = l.readlines()
#print (r)
kl=0
for linha in r:
    kl+=1;
    print (kl,linha)
    lista.append(linha)
l.close

print ('Lista inicial:', lista)

print ('Acrescentando Alunos à lista:')
nome = input (" nome ?")
while  nome!="":
    idade=input("idade ")
    lista.append([nome, idade]) #acrescenta à lista, uma lista com 2 elementos, nome e idade
    nome = input (" nome ?")

print ('Lista acrescentada:')
kl=0
for linha in r:
    kl+=1;
    print (kl,linha)
    lista.append(linha)
l.close

print ('Escrevendo a nova lista em ficheiro:')
f = open('pautanotas2.csv', 'w') 
w = csv.writer(f) 
lista=r


# escreve no ficheiro a lista
print (lista)
w.writerows(lista)
f.close()

print ('Estado Final:')
l=open('pautanotas.csv', 'r') 
r = l.read()
print (r)
for linha in r:
    print (linha)
l.close