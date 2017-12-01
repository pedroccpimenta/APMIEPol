# lista de números ímpares

impares1 = []
for i in range(100):
    if i % 2:
        impares1.append(i)
        
print ('Lista1 de números ímpares de 0 a 100:', impares1)
        
# Outra alternativa
impares2 = [i for i in range(100) if i % 2]
print ('Lista2 de números ímpares de 0 a 100:', impares2)


# outra alternativa:
impares3 = filter(lambda i: i % 2, range(100))
print ('Lista3 de números ímpares de 0 a 100:', *impares3)

#outra alternativa
impares4 = list(filter(lambda i: i % 2, range(100)))
print ('Lista4 de números ímpares de 0 a 100:', *impares4)

