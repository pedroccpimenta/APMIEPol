# eliminar vogais de um texto

def anti_vowel(text):
  a=''
  #print(text, len(text))
  #k=len(text)
  #print (type(k))
  for i in range(0, len(text)):
    x=text[i]  
    if x=='a' or x=='e' or x=='i' or x=='o' or x=='u' or x=='A' or x=='E' or x=='I' or x=='O' or x=='U':
            x=''
    else:
            a=a+x
    
  return(a)

b='As armas e os barões assinalados'
print(b, ":",anti_vowel(b))