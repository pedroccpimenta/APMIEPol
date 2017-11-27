"""
MoodyDJ

este programa vai ao ficheiro NVDecadas e escolhe as músicas com o grau de valencia emocional
(positivo/negativo) compativel com o que o utilizador indicou

Precisam de copiar para a pasta onde guardam este ficheiro, o searchYoutubeVideo.py
que contem o modulo que criei para procurar uma música no youtube.

Nota: Na eduroam, pode por vezes falhar ou dar erro ao tentar aceder à rede.

"""
import csv
import searchYoutubeVideo # modulo que criei para procurar musica no youtube
import webbrowser
#import time

f = open("NVDecades.csv", "r", encoding="utf-8")

f.readline() # ignora a linha de cabecalho
r =  csv.reader(f)

mood = input("Diga como se sente de 0 (negativo) a 1 (positivo) ?")
m = float(mood)

playlist = []

#cria uma playlist das musicas com o mood +/- 0.1 do utilizador 
for l in r:
    moodMusica = float(l[14]) #coluna com a valencia da musica
    if moodMusica > m - 0.1 and moodMusica < m + 0.1:
        playlist.append(l[16])
    
# percorre a lista playlist, procura o link no youtube e abre o link no browser
for musica in playlist:
    url = searchYoutubeVideo.search(musica) #procura no youtube pela string musica, retorna o link(url)
    print(url)
    webbrowser.open(url, 2) # abre o link, o 2 indica para abrir numa tab nova do browser
    #time.sleep(60)  #pode ser boa ideia parar uns segundos senão abre todas as janelas ao mesmo tempo
    
f.close()