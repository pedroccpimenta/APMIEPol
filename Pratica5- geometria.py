'''Escrever um programa para calcular a área e o volume de uma esfera, um cilindro ou um cone,
perguntando primeiro a geometria e, conforme a geometria, pedir as respectivas dimensões
características.

Porposta de resolução de Tatiana Pires

'''

from math import sqrt
        

geo = input ('Qual é a geometria? Esfera, Cilindro ou Cone ')
geo = geo.lower()
print(geo)

#Como posso fazer para este ciclo while funcionar apenas quando a minha string tiver um erro ortografico
#(ou um carater que nao era suposto) ?

# PCP - terá que incluir o cálculo (selectivo) 'dentro' do ciclo  no final, voltar a perguntar qual a
# (nova) geometria

# Altere o programa para indicar as unidades de medida do resultado (^2? ^3)
# Altere o programa de forma a que o Utilizador indique 'fim' para terminar (sair do ciclo)


while geo != ('esfera' or 'cilindro' or 'cone'):
    print ('A geometria nao está correta!')
    geo = input ('Qual é a geometria? Esfera, Cilindro ou Cone ')
    geo = geo.lower()
    print(geo)

    if geo == 'esfera':
        raio = input ('Raio da esfera = ')
        r = float(raio)
        area = 4*3.14*(r**2)
        volume = (4/3)*3.14*(r**3)
        print ('Area =', area, 'Volume =', volume)
    elif geo == 'cilindro':
        raio = input ('Raio da base do cilindro = ')
        altura = input ('Altura do cilindro =')
        r = float(raio)
        a = float(altura)
        area = 3.14*(r**2)*2 + 2*3.14*r*a
        volume = 3.14*(r**2)*a
        print ('Area =', area, 'Volume =', volume)
    
    elif geo == 'cone':
        raio = input ('Raio da base do cone = ')
        altura = input ('Altura do cone =')
        r = float(raio)
        a = float(altura)
        
        g = sqrt(r**2 + a**2)
        area = 3.14*(r**2) + 3.14*r*g
        volume = (1/3)*3.14*(r**2)*a
        print ('Area =', area, 'Volume =', volume)
    
    
    geo = input ('Qual é a geometria? Esfera, Cilindro ou Cone ')
    geo = geo.lower()