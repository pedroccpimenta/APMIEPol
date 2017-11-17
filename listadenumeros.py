

lista = [0]
import random

for i in range(1,10):
    lista.append(random.randint(100, 200))
    print('lista[',i, ']:', lista[i])    

soma=0
for i in range(1,10):
    if (lista[i]%2 == 0):
        soma=soma+lista[i]
        print (lista[i])
        
print ('soma dos pares:', soma)


produto=1
    
for i in range(1,10):
    if (lista[i]%2 == 1):
        produto=produto * lista[i]
        print (lista[i])
        
print ('produto dos ímpares:', produto)
