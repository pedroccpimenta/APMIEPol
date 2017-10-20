'''

Classificação de triângulos.

Dados os comprimentos dos três lados de um triângulo, o programa
deverá ser capaz de classificar o triângulo em equilátero, isósceles ou escaleno

'''

lado1=float(input('Comprimento do lado 1 ? '))
lado2=float(input('Comprimento do lado 2 ? '))
lado3=float(input('Comprimento do lado 3 ? '))

print ('lado 1:',  lado1, ', lado 2:',  lado2,', lado 3:', lado3)

if lado1==lado2 and lado2==lado3:
    print ("Triângulo equilátero")
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print ("Triângulo isósceles")
else:
    print ("Triângulo escaleno")
    
    
    
# 1. Verifique que o programa funciona bem

# 2. Que classificação o programa atribui ao tirângulo de lados {6, 7, 11} ?
# 3. Que classificação o programa atribui ao tirângulo de lados {7, 7, 7} ?
# 4. Que classificação o programa atribui ao tirângulo de lados {2, 5, 9} ?

# 5. Que melhorias sugere para este programa?
    
    
