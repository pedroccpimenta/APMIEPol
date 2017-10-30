"""
Elabore um algoritmo que dado um valor determinado valor em euros, calcule quantas moedas de:
 € 1  € 0.50   € 0.20  € 0.10   €0.05  €0.02  €0.01, serão necessárias para perfazer essa quantia (com o mínimo de moedas possível). 

NOTA: ao enunciado original acrescentei também a moeda de 2€
"""

moedas = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
q = input("valor em euros ? ")
valor = float(q)
for i in moedas:
    moeda = valor//i
    if moeda != 0:
        print("nº moedas de",i,"=",moeda)
    valor = valor%i # para não estar sugeito a erros de arrendondamento pode ser necessário arrendondar à 2 casa decimal valor = round(valor%i,2)
    
