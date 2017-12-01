#Bitwise Operations

print (5 >> 4)  # Right Shift
print (5 << 1)  # Left Shift
print (8 & 5)   # Bitwise AND
print (9 | 4)   # Bitwise OR
print (12 ^ 42) # Bitwise XOR
print (~88)     # Bitwise NOT


print (0b1),    #1
print (0b10),   #2
print (0b11),   #3
print (0b100),  #4
print (0b101),  #5
print (0b110),  #6
print (0b111)   #7
print ("******")
print (0b1 + 0b11)
print (0b11 * 0b11)


one = 0b1
two = 0b10
three = 0b11
four = 0b100
five =0b101
six =0b110
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven =0b1011
twelve =0b1100


# print out the binary representations of the numbers 2 through 5, each on its own line.

for n in range(2,6):
  print (n, bin(n))
  
  
# Função int(, base)
print (int("1",2))
print (int("10",2))
print (int("111",2))
print (int("0b100",2))
print (int(bin(5),2))
# Print out the decimal equivalent of the binary 11001001.
print (int('11001001',2))

# Shift
shift_right = 0b1100
shift_left = 0b1

# Your code here!
shift_right=shift_right >> 2
shift_left =shift_left <<2

print (bin(shift_right))
print (bin(shift_left))

# print format
print (0b1110 | 0b101)
print (bin(0b1110 | 0b101))

# Operador ^
#Using the XOR (^) operator 
print (bin(0b1110 ^ 0b101))

#Define a function, check_bit4, with one argument, input, an integer.

#It should check to see if the fourth bit from the right is on.
#If the bit is on, return "on" (not print!)
#If the bit is off, return "off".

def check_bit4(input):
    answer=input & 0b1000
    if answer > 0:
        return 'on'
    else:
        return 'off'
    
    
print (check_bit4(10))    


# Using the XOR (^) operator is very useful for flipping bits. Using ^ on a bit with the number one will return a result where that bit is flipped.

