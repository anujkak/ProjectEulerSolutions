"""This one I get to use list comprehensions because Python offers an easy 1 line method for creating lists instead of making a for loop and iterating"""
sum_of_the_squares = sum([x**2 for x in range(101)])   #All the numbers from 1-100 squared and then added
square_of_the_sums = (sum([x for x in range(101)])**2) # All the numbers from 1-100 added then squared
print  square_of_the_sums - sum_of_the_squares #Subtracting the added then squared from squared then added
#The variable names got  unwieldy, so I'm probably going to go back and change them later. This is problem 6 for project euler. 
