my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")


for x in my_list:
  my_file.write(str(x)+'\n')
    
my_file.close()

my_file=open('output.txt', 'r')

print (my_file.read())

my_file.close()


# Leitura de um ficheiro linha a linha
my_file=open('text.txt', 'r')

print (my_file.readline())
print (my_file.readline())
print (my_file.readline())


my_file.close()

