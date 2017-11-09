def f(x):
    return x**2

def integra(funcao, a, b, samples):
    """ Faz uma aproximação númerica do integral de uma função(x)
        entre os valores a e b, dividindo o intervalo no número de samples"""
    
    l = [x / samples for x in range(a*samples,b*samples,1)]
    
    integral = 0
    for x in l:
        integral += f(x)/samples
    
    return integral

print ( integra(f, 0, 2, 1000))
