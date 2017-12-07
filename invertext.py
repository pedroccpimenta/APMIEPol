my_file=open('t1.txt', 'r')

l1=my_file.readlines()

print (l1)

my_file.close()

nc=[]
for l in l1:
    nl=''
    #print (len(l), l)
    for i in range(0,len(l)):
        #print (i)
        if l[len(l)-i-1]!='\n':
            nl=nl+l[len(l)-i-1]
        
    nl=nl+'\n'
    print (nl)
    nc.append(nl)
    
print ('Novo conteúdo do ficheiro:')
print (nc)

my_file=open('t2.txt', 'w')
my_file.writelines(nc)
my_file.close()
    
