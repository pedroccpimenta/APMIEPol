"""
    inteiro ou decimal
"""

n = input("Numero?")
numDecimal = float(n)

# o truque é ver se o número convertido para inteiro é igual ao número convertido para float
numInteiro = int(numDecimal)
if numDecimal==numInteiro:
    print("número inteiro")
else:
    print("número decimal")

