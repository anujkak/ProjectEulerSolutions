"""my_list = range(1,21)
list_check = 0
def number_iterator():
    number_count = 0
    while list_check < 20:
        number_checker()
        number_count += 1
    if list_check == 20:
        print number_count
def number_checker():
    number_count = 0
    for i in my_list:
        list_check = 0
        if number_count % i == 0:
            list_check += 1
number_iterator()
"""
#So I found that there was an easier way to solve this problem that didn't require code at all. You already know the number that all numbers 
#1 - 10 evenly divide into(2520). Then you have to find the product of all primes from 11-20 and multiply it with 2520 and 2. 
# You need 2 because 2 also factors into the numbers twice. 20 -> 5*4 & 10* 2. 
#The answer comes out to 232792560. Hope this helped!