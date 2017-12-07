m = [1, 2, 3]
n = [4, 5, 6]

# Add your code here!
def join_lists (a,b):  
  c=a
  for i in b:
    c.append(i)
  return (c)

print ('1:',join_lists(m, n))

def join_lists2 (a,b):
  return (a+b)

print ('2:',join_lists2(m, n))

# Como explica o resultado do último print ?
# Tatiana - A função join_lists utiliza as listas m e n, e devolve uma lista c que é a junçao à lista m os valores de n.
# Tatiana - Enquanto a função join_lists2 utiliza uma lista que foi modificada na primeira função (lista c que é igual à lista (m+n)), 
# assim a soma da lista a com b é como se fosse a soma de (m+n)+n .
