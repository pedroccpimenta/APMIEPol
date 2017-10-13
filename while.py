answer = input('Dá-me um número: ')

# As instruções que pertencem ao ciclo while são definidas pela indentação em relação
# à palavra while

print ('Primeira modo')
a = 0
while a < int(answer):
  a += 1
  print(a)
  
  
print ('Segundo modo')
# neste caso, a instrução 'print(a)' não é executada durante o ciclo - só é
# executada 'após' o ciclo estar complet
a = 0
while a < int(answer):
  a += 1
  
print(a)