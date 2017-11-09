def f(x):
    return x**2

l = [x / 100 for x in range(0,200,1)]
    
integral = 0
for x in l:
    integral += f(x)*0.01
    
print("Aproximação numérica do integral", integral)
print("Valor do integral:", 2**3/3)
print("Erro ", integral-2**3/3)
