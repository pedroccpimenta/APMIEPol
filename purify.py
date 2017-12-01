# Retirar determinadoselementos de uma lista

def purify(lista):
    b=[]
    for x in lista:
        if x%2==0:
            b.append(x)
        
    return(b)



print (purify([2,5,6,5,7,9,87,89,2]))