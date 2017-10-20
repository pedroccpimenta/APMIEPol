'''
O Cálculo do Factorial é um exemplo clássico utilizado na aprendizagem de programação,
porque permite a exploração de vários conceitos-base, tais como ciclo (várias alternativas), função e recursividade

Factorial - função
Na eventualidade de querermos calcular o factorial de várias variáveis - como, por exemplo,
em cálculo de probabilidades, torna-se cómodo utilizar uma função que simplifique a escrita
dos programas

'''

def  factorial(x):
    f=1
    i=1
    while i<=x:
        f=f*i
        i+=1
    return(f)
    

n=input('Introduza o valor N do qual pretende calcular o factorial ? ') # input devolve uma string
n=int(n) # temos que converter a string n num valor inteiro para podermos utilizar o ciclo while das
         # linhas seguintes

print (n,'!=',factorial(n))




