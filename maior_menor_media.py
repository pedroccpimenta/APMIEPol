"""

Elabore um programa em Python que depois de ler uma sequência de N números (N também pedido ao utilizador),
apresente os seguintes resultados:
    máximo, mínimo, somatório,
    a quantidade de números superiores a 10,
    a percentagem de valores superiores a 10,
    a média, a média dos valores superiores a 10.
"""

l = []   # lista vazia onde vamos guardar os números a ler do utilizador
lmaior10 = []  # esta vai só guardar os numeros superiores a 10

n = input("Quantos números vamos ler?")
num = int(n)

for i in range(num):
    n = input("Numero ? ")
    num = int(n)
    l.append(num)
    if num > 10:   # se o numero é superior a 10 acrescenta-o tambem a outra lista
        lmaior10.append(num)
          
print("Máximo", max(l))
print("Minimo", min(l))
print("Somatório ", sum(l))
print("Media ", sum(l) / len(l))
print("Quantidade de números superiores a 10", len(lmaior10))
print("Media de números superiores a 10", sum(lmaior10)/len(lmaior10))


