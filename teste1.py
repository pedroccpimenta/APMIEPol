print("------------------ Pergunta 1")
a=int(input("numero: "))
b=str(a)

print (type(b))


print ("------------------ Pergunta 2")
c=10
v=0
while c>4:
    v=v+1
    print(c)
    c=c-1
print("C=", c)
print ("O ciclo foi executado ",v,"vezes")

print ("------------------ Pergunta 3")

print ("------------------ Pergunta 4")
a,b,c,d=0,2,0,8
for i in range(b,d):
    if d*a<20:
        c=c+1
    print('a=',a,'c=',c)


print ("------------------ Pergunta 5")
l=list(range(25,100,5))
print(l)

print ("------------------ Pergunta 6")

n=5;s=0
for i in range(1,n+1):
    s=s+2**i
print (s)
compa=2**1+2**2+2**3+2**4+2**5
print (s,compa)

print ("------------------ Pergunta 7")

print ("------------------ Pergunta 8")
print ("------------------ Pergunta 9")

a=[10,9,8,6,4,2,1]
print (a[0])
c=0;i=1
while i<6:
        if a[i] > 4:
            print (c)
        c=c+2
        i=i+1
            
print ("------------------ Pergunta 11")

a=5
n=5
mult=1
compa=1*3*5*7*9
while a>n-5:
    mult=mult*(2*a-1)
    a=a-1
print('O produto dos 1ºs 5 ímpares é: ', mult, 'comparação: ', compa)
    
print ("------------------ Pergunta 12")

r = 10//3
print ('r: ', r)

print ("------------------ Pergunta 13")
menu=['vitela', 'sardinha', 'coelho', 'frango']
menu.sort()
menu.insert(len(menu), 'tarte de maça')
del menu[-2]
menu.append('café')

print (menu)

print ("------------------ Pergunta 14")
l=6
j=12

print ('a)', not(l>5 or j<8))
print ('b)', i!=6 or l>0 and j<13)
print ('c)', l>=6 and (l==6 or j>5))
print ('d)', l<4 or j>5)


print ("------------------ Pergunta 15")

peso=float(input('peso'))
altura=float(input('altura'))

imc=peso/(altura**2)
print('imc:', imc)
if imc>=18.5 and imc <=25:
        print('ok para futebol')
else:
        print ('not ok para futebol')


print ("------------------ Pergunta 16")
import random

lista=list(range(10))
print (lista)

for i in range(10):
    lista[i]=random.randint(5,50)
    
c=0
produto=1
for i in range(10):
    if lista[i] % 2==1:
        c=c+1
        produto=produto*lista[i]
        
print ('contador:', c, 'produto:', produto)
    

    
    
print (lista)