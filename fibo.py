def fibo(n):
    if n==1 or n==2:
        return(1)
    else:
        return(fibo(n-1)+fibo(n-2))
    

for x in range(1,15):
    print ('F',x, ":", fibo(x))