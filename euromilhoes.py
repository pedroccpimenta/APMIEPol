"""
Sorteio de uma chave de euromilhões - 5 números distintos de 1 a 50

"""

import random

# simulação da aposta sobre um boletim 'vazio/por preencher'
# criação da matriz 'vazia' - as casas de 1 a 50 estão 'por preencher' (0)

p=[0] # De momento, criaremos uma lista com 51 elementos, para podermos
      # usar os elementos de índice 1 a 50

for i in range (1, 51):
    p.append(0)
   # print (p[i])
        
        
# Inicialização dos elementos da lista a 0 ('por preencher')
print("Estado inicial do boletim do euromilhões:")
for i in range (1,51):
    print (p[i] , " ", end='') # end='' previne a mudança de linha
    

# Sorteio de valores inteiros, de 1 a 50
c=0
while c<5:
    q=random.randint(1, 50)
    print(q)
    if (p[q] == 0):  # se a posição 'q' está 'por preencher' (0), 'preenchemo-la' / marcamo-la (1)
        p[q]=1
        c=c+1        # só quando marcamos uma posição de novo, incrementamos o contador
                     # se saírem números repetidos, só o primeiro é tido em consideração
        
                
# Estado final do boletim    
print("Estado final do boletim do euromilhões:")
for i in range (1,51):
    print (p[i] , " ", end='')


# Escrita da chave do euromilhões, por ordem crescente
print("Chave:")
for i in range (1,51):
    if (p[i]==1):
        print (i , " ", end='')

