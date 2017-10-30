"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo. 
"""

n = input("numero?")
num = int(n)

# se o numero introduzido for maior que 1000 continua a pedir 
while num > 1000:
    n = input("numero?")
    num = int(n)
    
centenas = num // 100    # o simbolo // é a divisão inteira
num = num - centenas*100   # podia também fazer o resto da divisão tal como no exerc. das moedas num = num % centenas
dezenas = num // 10
num = num - dezenas * 10
unidades = num  
print(centenas, "centenas,", dezenas, "dezenas e", unidades, "unidades")   
