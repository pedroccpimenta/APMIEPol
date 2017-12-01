# Verificar se um dado número é primo
# A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself.


def is_prime(x):
    if x<2:
        return False
    else:
        for n in range (2, x-1):
            if x%n == 0:
                return False
            
        return True
    
    
print ('8 is prime?:',is_prime(8))
print ('17 is prime?', is_prime(17))

print ('1 is prime?', is_prime(1))