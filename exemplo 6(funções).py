#1
def f(nome, idade):
    print(nome,'tem',idade,'anos')
    return

# duas formas diferentes de invocar a função f() # Comentário PCP
f('maria',18)
          
nome="Maria"
idade="20"
f(nome, idade)


#2 - re-definição da função f() # Comentário PCP
def f(nome, idade):
    anonascimento=2017-idade
    
    print(nome,'tem',idade,'anos','nascida no ano de', anonascimento)
    return anonascimento

anon=f('maria',18)
print ("Ano de nascimento:", anon)



#3 - re-re-definição da função f() # Comentário PCP
def f(nome, idade):
    anonascimento=2017-idade
    print(nome,'tem',idade,'anos','nascida no ano de', anonascimento)
    return
    
f('maria',18)



          