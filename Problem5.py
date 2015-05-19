my_list = range(1,21)
global number_count = 0
global list_check = 0
def number_iterator():
    while list_check < 20:
        
        number_checker()
        number_count += 1
    if list_check == 20:
        print number_count
def number_checker():
    for i in my_list:
        list_check = 0
        if number_count % i == 0:
            list_check += 1
number_iterator()
#FinishTmrw. 