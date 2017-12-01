# Mediana de uma lista

def median(lista):
    lista=sorted(lista)
    
    print('lista, len lista:',lista, len(lista))
    if len(lista)%2==1:
        median=lista[int((len(lista)-1)/2)]
    else:
        median=lista[int((len(lista))/2)]+lista[int((len(lista))/2-1)]
        median=float(median/2.)
            
    return(median)



print (median([5,7,19]))

print (median([5,7,19,20]))

print (median([4,5,5,4]))
