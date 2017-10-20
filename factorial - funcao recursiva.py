'''
O Cálculo do Factorial é um exemplo clássico utilizado na aprendizagem de programação,
porque permite a exploração de vários conceitos-base, tais como ciclo (várias alternativas), função e recursividade

Factorial - função recursiva

'''

def  factorial(x):
    if x<=1:
        return (1)
    else:
        return x*factorial(x-1)

n=input('Introduza o valor N do qual pretende calcular o factorial ? ') # input devolve uma string
n=int(n) # temos que converter a string n num valor inteiro para podermos utilizar o ciclo while das
         # linhas seguintes

print (n,'!=',factorial(n))




