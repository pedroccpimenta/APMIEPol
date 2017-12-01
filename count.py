#Contar elementos de uma lista que obedeçam a determinadas condições

def count(sequence, item):
    conta=0
    print('seq:', sequence)
    for i in sequence:
        #print(i)
        if i==item:
            conta+=1
            
    return(conta)
     
print ('contagem 3:',count([5, 6, 5, 3, 5, 6], 3))
print ('contagem 5:',count([5, 6, 5, 3, 5, 6], 5))

print ('contagem [2, 9]:',count([5, 6, 5, 3, [2,9], 5, 6], [2,9]))
