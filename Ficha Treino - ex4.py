''' 4. Escreva um programa que solicite ao utilizador um número até 99 e imprima-o no ecrã
por extenso.

Objetivo - Encontrar uma versão mais simplificada em alternativa ao meu código
 '''

numero = int(input('Dá-me um número até 99:'))

dezenas = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta',\
           'noventa']
n = ['zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
d = ['dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezasseis', 'dezassete',\
     'dezoito', 'dezanove']

def extenso(numero):
    if numero >=0 and numero <= 9:
        print(n[numero])
    elif numero >=10 and numero <= 19:
        numero = str(numero)
        for i in range(0,10):
            if i == int(numero[1]):
                print(d[i])
    else:
        numero = str(numero)
        if int(numero[1]) == 0:
            for i in range(0,10):
                if i == int(numero[0]):
                    print(dezenas[i - 2])
        else:
            for i in range(0,10):
                if i == int(numero[0]):
                    parte1 = dezenas[i - 2]
            for j in range(1, 10):
                if j == int(numero[1]):
                    parte2 = n[j]
                            
            print(parte1, 'e', parte2)       
            
print(extenso(numero))
