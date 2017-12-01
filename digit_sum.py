def digit_sum(n):
  soma=0
  while n > 0:
    soma+=n%10
    n=int(n/10)
    print (soma, n)
  return(soma)


print (digit_sum(int(1311)))