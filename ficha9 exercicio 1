#joao carneiro A79704

import csv


f=open('NVDecades.csv','r',encoding='utf-8')
f.readline()
r=csv.reader(f)

max=0

for l in r:
    print(l[len(l)-2])
    
    duration = float(l[len(l)-6])
    musica = l[len(l)-2]
    
    if duration>max:
        max=duration
        musicamaislonga=musica
print('a musica mais longa é:',musicamaislonga,'com duração de,',duration)

#nao aparece a duraçao correta
#PCP / porque não está a imprimir a variável correcta - deverá imprimir max e não duration
print('a musica mais longa é:',musicamaislonga,'com duração de,',max)
# Indique também qual a unidade de tempo
# converta a duração para unidades mais comuns, como minutos: segundos
