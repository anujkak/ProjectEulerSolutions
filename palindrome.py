import random
def numbermultiplier():
    my_list= range(100,1000) #List of 3 digit integers to multiply random integer permutations. 
    multiplied_values = [] #Empty list to store data values that palindrome checker returns True
    max_count = 807302#Maximum amount of possible permutations of 3 digit integers being multiplied. 899!/879!
    counter_number = 0 #Counter for while loop
    while counter_number < max_count:
        counter_number += 1
        y = random.choice(my_list) * random.choice(my_list) #used randint to pick a integers to multiply
        if palindromechecker(y) == True: 
            multiplied_values.append(y)
    print max(multiplied_values)
def palindromechecker(x):
    if str(x) == str(x)[::-1]:#Inverts the strings
        return True
numbermultiplier()
