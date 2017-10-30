"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

v=['a','e','i','o','u']
c=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
 
letra = input("Letra ? ")
 
if letra.lower() in v:  # O lower converte a string para minúsculas.
                        # Isso assegura que mesmo que o utilizador tenha introduzido uma letra maiúscula o programa funciona
    print ("A letra ", letra, " é uma vogal.")
else:
    print ("A letra", letra, "é uma consoante.")
 