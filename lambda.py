# Lambda - anonymous function

languages = ["HTML", "JavaScript", "Python", "Ruby"]

# Add arguments to the filter()
print (*filter(lambda x:x=='Python', languages))


#
#Create a list, squares, that consists of the squares of the numbers 1 to 10. A list comprehension could be useful here!
#
#Use filter() and a lambda expression to print out only the squares that are between 30 and 70 (inclusive).

squares=[x**2 for x in range(1,11)]

print(*filter (lambda x:x<=70 and x>=30, squares))

# Call the appropriate method on movies such that it will print out all the items (hint, hint) in the dictionary—that is, each key and each value.
movies = {
  "Monty Python and the Holy Grail": "Great",
  "Monty Python's Life of Brian": "Good",
  "Monty Python's Meaning of Life": "Okay"
}


print (movies.items())


# divisívies por 3 ou por 5
threes_and_fives=[x for x in range(1,16) if x%3==0 or x%5==0]

print(threes_and_fives)


#mensagem escondida

# The string in the editor is garbled in two ways:
# Our message is backwards.
#The letter we want is every other letter.
# Use list slicing to extract the message and save it to a variable called message.

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"


message=garbled[::-2]

print (message)



#Create a new variable called message.
#
#Set it to the result of calling filter() with the appropriate lambda that will filter out the "X"s. The second argument will be garbled.
#
#Finally, print your message to the console.

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"


message=filter(lambda x: x!='X', garbled)

print(*message)
