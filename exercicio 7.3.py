#Sónia Machado
import csv
f= open('pautaNotas exercicio 7.3.csv', 'r+', enconding='utf-8')
r=csv.reader(f)
soma=0

for l in r:
    print(l[2])
    n=float(l[2])
    soma+=n
    
media=soma/len(l[2])
print(' média dos alunos é:', media)
    
    
print(soma/len(l))