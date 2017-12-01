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