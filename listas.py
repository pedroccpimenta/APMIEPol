#Operações com listas

my_list = range(1, 11)

# Add your code below!
backwards=my_list[::-1]
print(backwards)

# Outro exemplo
to_one_hundred = range(101)

backwards_by_tens= to_one_hundred[::-10]
print(backwards_by_tens)

#Create a list, to_21, that's just the numbers from 1 to 21, inclusive.
#Create a second list, odds, that contains only the odd numbers in the to_21 list (1, 3, 5, and so on). Use list slicing for this one instead of a list comprehension.
#Finally, create a third list, middle_third, that's equal to the middle third of to_21, from 8 to 14, inclusive.

to_21 = range(1,22)
odds=to_21[::2]

print (odds)

middle_third=to_21[7:14]
print (middle_third)


