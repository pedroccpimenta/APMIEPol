#Sónia Machado
import csv
f= open('pautaNotas.csv', 'r+', encoding='utf-8')
# PCP - não é 'enconding', é 'encoding'

# PCP - para ler a 1ª linha - cabeçalho da tabela - sem tentar interpretar o conteúdo
k=f.readline() 

r=csv.reader(f)
soma=0

for l in r:
    print(l[2])
    n=float(l[2])
    soma+=n
    
media=soma/len(l[2])
print(' média dos alunos é:', media)
    
    
print(soma/len(l))

# PCP - deve imprimir os resultados aos poucos, para ter a certeza dos cálculos que está a efectuar:
print ('soma:', soma)
# PCP - Soma está bem calculada?

#PCP - para dividir a soma pelo número de alunos, o que deveria usar?
print ('len(l[2])',len(l[2]))
# PCP - o que é o len - comprimento - de l[2] ?


print ('len(l)',len(l))
# PCP - o que é o len - comprimento - de l ?

# Como pode chegar ao fim do ciclo for e conhecer o número de alunos na lista?
