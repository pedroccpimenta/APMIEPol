"""
Processa o ficheiro NVDecades.csv

Faz plot da dançabilidade ao longo das décadas:

cada linha contêm:

0         1           2  3   4      5        6      7           8            9                10   11             12       13       14      15           16    17
artist_id	artist_name	id	key energy	liveness	tempo	speechiness	acousticness	instrumentalness	mode	time_signature	duration	loudness	valence	danceability	title	decade

"""

import csv
import matplotlib.pyplot as plt    # importa o módulo de gráficos (as plt para abreviar o nome)

f = open("NVDecades.csv", "r", encoding="utf-8")

f.readline()    # ignora a primeira linha (cabeçalho)

r = csv.reader(f)

dance = []  # lista a preencher com a dançabilidade de cada música
decade = [] # lista com a decada da música respetiva 

for l in r:
    dance.append(float(l[15])) # converte o valor da dancabilidade para float e guarda na lista
    decade.append(l[17])
        
plt.plot(decade, dance, ".")
plt.show()

f.close()
