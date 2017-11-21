# exemplo de codeacademy
# Pedro Pimenta, Nov. 2017

shopping_list = {"banana":1, "orange":10, "apple":1}

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}
    
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

# Write your code below!
def compute_bill(food):
    total=0
    c=0
    for x in food:
        c=c+1
        if stock[x] > 0:
            total=total+prices[x]
            stock[x]=stock[x]-food[x]
            print('c:', c, ", ", total)
    
    return total
 
print (compute_bill(shopping_list))
print (stock)