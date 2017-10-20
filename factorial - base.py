'''
O Cálculo do Factorial é um exemplo clássico utilizado na aprendizagem de programação,
porque permite a exploração de vários conceitos-base, tais como ciclo (várias alternativas), função e recursividade

'''

n=input('Introduza o valor N do qual pretende calcular o factorial ? ') # input devolve uma string
n=int(n) # temos que converter a string n num valor inteiro para podermos utilizar o ciclo while das
         # linhas seguintes

f=1
i=1
while i<=n:
    f=f*i
    i+=1
    
print (n,'!=',f)




