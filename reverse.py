def reverse(text):
  a=''
  print(text, len(text))
  k=len(text)
  print (type(k))
  for i in range(0, k):
    x=text[i]  
    print(i,x, a)
    a=a+text[len(text)-i-1]
    
  return(a)

b='As armas e os barões assinalados'
print(b, ":",reverse(b))