# Produto dos elementos de uma lista

def product(lista):
    produto=1
    for x in lista:
        produto*=x
    return produto



print(product([8, 3,5]))
