"""
Exercicio 4 Algoritimia e Programação 2017/18

Blackjack

O computador sorteia a sua mão de 3 cartas do baralho, apresentando no ecrã cada carta e a soma total do valor das cartas. Se ultrapassar 21 imprimir “Estorei !”.

De seguida é sorteada uma carta para o jogador, é apresentada a carta e pedido se quer nova carta. O jogador poderá pedir tantas cartas quantas quiser. Se ultrapassar 21 estoura.

Ganha quem se aproximar mais de 21 mas sem ultrapassar! 

O valor das cartas vai de 1 a 13, correspondendo ao valor do Ás, 2, 3, ... Valete, Dama e Rei respetivamente.
Estes valores não correspondem às regras originais do jogo mas permitem simplificar o programa.

Pedro Branco

"""

import random
naipe = ["Paus", "Ouros", "Copas", "Espadas"]
numero = ["Ás", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Valete", "Dama", "Rei"]

totalComputador = 0
    
print("--- Computador ---")
#sortear 3 cartas do baralho
for i in range(3):
    naipeSorteado = random.randint(0, len(naipe)-1)
    numeroSorteado = random.randint(0, len(numero)-1)

    print(str(numero[numeroSorteado]) + " " + naipe[naipeSorteado])
    totalComputador += (numeroSorteado + 1)
    
# apresenta o total
print (totalComputador)
if totalComputador > 21:
    print("Estourei !")


print("--- Jogador ---")

# escolhe 1 carta para o utilizador
naipeSorteado = random.randint(0, len(naipe)-1)
numeroSorteado = random.randint(0, len(numero)-1)
print(str(numero[numeroSorteado]) + " " + naipe[naipeSorteado])

outraCarta = input("Outra carta ? (S/N)")
totalJogador = numeroSorteado + 1

while (outraCarta == "S" or outraCarta == "s") and totalJogador < 21:
    naipeSorteado = random.randint(0, len(naipe)-1)
    numeroSorteado = random.randint(0, len(numero)-1)
    print(str(numero[numeroSorteado]) + " " + naipe[naipeSorteado])

    outraCarta = input("Outra carta ? (S/N)")
    totalJogador += (numeroSorteado + 1)
    
print (totalJogador)

if totalJogador > 21:
    print("Jogador Estourou !")
    
# Verifica quem ganhou 
if totalComputador > 21 and totalJogador > 21:
    print("Ninguém ganhou ")
elif totalComputador > 21:
    print("Jogador ganhou !")
elif totalJogador > 21:
    print("Computador ganhou ")
elif (21 - totalComputador) > (21 - totalJogador):
    print("Jogador ganhou !")
else:
    print("Computador ganhou ")
    
    
    