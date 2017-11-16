#qual seria a melhor forma de evitar estar a escrever o 'if' varias vezes, usando um função?(e mantendo a percentagem p)

import random

naipe = ['Paus', 'Ouros', 'Copas', 'Espadas']
carta = ['Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']

totalPC = 0
totalEu = 0
c = 0; n = 0
p = 0
r = 's'

while totalPC <= 21 and totalEu <= 21:
    if totalPC == 0 and p != 1:
        c = random.randint(0,12)
        totalPC = totalPC + c + 1
        n = random.randint(0,3)
        if c == 11:
            print('A primeira carta do computador é: a', carta[c], 'de', naipe[n], '........(', totalPC, ')')
        elif c != 11:
            print('A primeira carta do computador é: o', carta[c], 'de', naipe[n], '........(', totalPC, ')')
    
    elif totalPC < 9 and totalPC != 0 and p != 1:
        c = random.randint(0,12)
        totalPC = totalPC + c + 1
        n = random.randint(0,3)
        if c == 11:
            print('A nova carta do computador é: a', carta[c], 'de', naipe[n], '........(', totalPC, ')')
        elif c != 11:
            print('A nova carta do computador é: o', carta[c], 'de', naipe[n], '........(', totalPC, ')')
    
    elif totalPC >= 9 and totalPC < 13 and p != 1:
        p = random.randint(1,16)
        if p == 1:
            print('O PC parou de jogar.')
        else:
            c = random.randint(0,12)
            totalPC = totalPC + c + 1
            n = random.randint(0,3)
            if c == 11:
                print('A nova carta do computador é: a', carta[c], 'de', naipe[n], '........(', totalPC, ')')
            elif c != 11:
                print('A nova carta do computador é: o', carta[c], 'de', naipe[n], '........(', totalPC, ')')
                
    elif totalPC >= 13 and totalPC < 18 and p != 1:
        p = random.randint(1,2)
        if p == 1:
            print('O PC parou de jogar.')
        else:
            c = random.randint(0,12)
            totalPC = totalPC + c + 1
            n = random.randint(0,3)
            if c == 11:
                print('A nova carta do computador é: a', carta[c], 'de', naipe[n], '........(', totalPC, ')')
            elif c != 11:
                print('A nova carta do computador é: o', carta[c], 'de', naipe[n], '........(', totalPC, ')')
                
    elif totalPC >= 18 and totalPC < 21 and p != 1:
        x = random.randint(1,20)
        if x != 1:
            p = 1
        else:
            p = 2
        if p == 1:
            print('O PC parou de jogar.')
        else:
            c = random.randint(0,12)
            totalPC = totalPC + c + 1
            n = random.randint(0,3)
            if c == 11:
                print('A nova carta do computador é: a', carta[c], 'de', naipe[n], '........(', totalPC, ')')
            elif c != 11:
                print('A nova carta do computador é: o', carta[c], 'de', naipe[n], '........(', totalPC, ')')
    
    while totalPC < totalEu and p != 1:
        c = random.randint(0,12)
        totalPC = totalPC + c + 1
        n = random.randint(0,3)
        if c == 11:
            print('A nova carta do computador é: a', carta[c], 'de', naipe[n], '........(', totalPC, ')')
        elif c != 11:
            print('A nova carta do computador é: o', carta[c], 'de', naipe[n], '........(', totalPC, ')')
    
    if r != 'n':
        r = input('Queres tirar alguma carta (S/N)?')
        while r != 's' and r != 'S' and r != 'n' and r != 'N':
            r = input('A resposta têm de ser válida: (S) ou (N)')
        r.lower()
        if r == 's':
            c = random.randint(0,12)
            totalEu = totalEu + c + 1
            n = random.randint(0,3)
            if c == 11:
                print('A tua carta é: a', carta[c], 'de', naipe[n], '----->(', totalEu, ')')
            if c != 11:
                print('A tua carta é: o', carta[c], 'de', naipe[n], '----->(', totalEu, ')')
        if r == 'n':
            print('Paraste de jogar.')
    print(' ')
    
    if totalPC > totalEu and r == 'n':
        break
    if totalPC < totalEu and p == 1:
        break
    if r == 'n' and p == 1:
        break

if totalEu > 21:
    print('Jogador Estourou!')
if totalPC > 21:
    print('Computador Estourou!')
    
if totalPC > 21 and totalEu > 21:
    print("Ninguém ganhou...")
elif totalPC > 21:
    print("Jogador ganhou! :)")
elif totalEu > 21:
    print("Computador ganhou! :(")
elif totalEu = totalPC:
    print('Empate')
elif (21 - totalPC) > (21 - totalEu):
    print("Jogador ganhou! :)")
else:
    print("Computador ganhou! :(")