
    #So if you have a prime number, you are gonna want to keep dividing it by number until you reach the largest possible number to divide it by.
    #Part of the problem is that I cannot decide if I want to use a recursive method, or if it would be smarter to just do a while loop.
currentprimefactor = 0
factors_array = []
y = 0
primenumber = 600851475143
while currentprimefactor < primenumber: 
    y = primenumber/(currentprimefactor + 1)
    if isinstance(y , int) == True:
        factors_array.append(y)
print max(factors_array)

