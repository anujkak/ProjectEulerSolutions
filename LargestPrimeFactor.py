

currentprimefactor = 0
factors_array = []
y = 0
primenumber = 600851475143
while currentprimefactor < primenumber: 
    y = primenumber/(currentprimefactor + 1)
    if isinstance(y , int) == True:
        factors_array.append(y)
print max(factors_array)

