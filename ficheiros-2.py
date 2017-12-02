with open('text.txt', 'r+') as my_file:
  my_file.write ('outra linha de texto')
  if not my_file.closed:
    my_file.close()
    
    
  print (my_file.closed)
  
  
  
  # Leitura de um ficheiro linha a linha
my_file=open('text.txt', 'r')

print (my_file.readline())
print (my_file.readline())
print (my_file.readline())


my_file.close()