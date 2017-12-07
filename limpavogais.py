def limpa (frase):
        r=()
        for letra in frase:
            if letra=='a' or letra=='e' or letra=='i' or letra =='o' or letra=='u':
                r+='.'
            else:
                r+=letra
            
        return (r)
    
original='exemplo de frase a ser tratada'
    
limpa=limpa(original)
print('original:', original)
print('resultado:', limpa)