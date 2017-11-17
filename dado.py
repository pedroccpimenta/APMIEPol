
import random

d=random.randint(1, 6)

print ('Dado:', d)


contamax=0
for i in range (1, 20):
    d=random.randint(1, 6)
    if (d==6):
        contamax = contamax + 1
    
print ('o valor 6 saiu',contamax,'vezes.')