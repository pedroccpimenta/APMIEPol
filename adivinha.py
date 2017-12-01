from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!

guess=int(input('a guess?'))

while guesses_left >0:
    print ('guesses_left:', guesses_left)  
    guesses_left-=1
    if guess==random_number:
        print ('congratulations! You win!')
        break
    guess=int(input('another guess?'))	
else:
    print ('You lose.')
         