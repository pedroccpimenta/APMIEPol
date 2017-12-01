# Processar texto de forma a eliminar determinadas palavras


def censor(text, word):
    resultado=''
    palavras=text.split(' ')
    print ('Palavras:',palavras)
    for i in range(len(palavras)):
        if palavras[i]==word:
            palavras[i]="*" * len(word)
            print('p:',palavras[i])
            
    resultado=" ".join(palavras)
  
    return (resultado)

    
print (censor("As armas e os barões assinalados", 'barões'))