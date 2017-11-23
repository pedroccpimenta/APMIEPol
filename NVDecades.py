"""
Processa o ficheiro NVDecades.csv
com os dados do top 100 das músicas de cada decada (1950 até 2009) com vários atributos de cada música
https://github.com/nvempala/Music-Decades-Top-100

cada linha contêm:

0         1           2  3   4      5        6      7           8            9                10   11             12       13       14      15           16    17
artist_id	artist_name	id	key energy	liveness	tempo	speechiness	acousticness	instrumentalness	mode	time_signature	duration	loudness	valence	danceability	title	decade

O programa imprime a música mais dançável destas 6 decadas.
"""
import csv

f = open("NVDecades.csv", "r", encoding="utf-8")

f.readline() # ignora a primeira linha (cabeçalho)

r = csv.reader(f)

dancabilityMax = 0 # variável que guarda o grau de dancabilidade máxima

for l in r:
    dancability = float(l[15])
    if dancability > dancabilityMax:
        # se a dancability é maior que dancabilityMax, encontrou um novo maximo
        dancabilityMax = dancability
        artista = l[1]
        musicaDancabilidadeMax = l[16]
        
print("A música mais dançável é:", musicaDancabilidadeMax, "com", dancabilityMax, "de", artista)
f.close()