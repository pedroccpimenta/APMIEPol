# Remover elementos duplicados de uma lista

def remove_duplicates(lista):
    b=[]
    for x in lista:
        if x not in b:
            b.append(x)
            
    return(b)



print(remove_duplicates([5,6,7,2,3,2,2,1,1,2,7,8,21]))