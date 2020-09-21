#It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

#Notes
#There are no solutions under 100000 so that there are 6 places for digits to be swapped around 
#Thanks to a search the difference between permuations is always a multiple of 9 therefore we can iterate by 9 starting with a number that is divisible by 9 hence starting with 100008
import timeit


def perm_check(number):
    for x in range(2,6,1):
        if sorted(str(number)) == sorted(str(x*number)):
            continue 
        else:
            return False
    return True

def Problem_52():
    i=100008
    solution = False
    while solution == False:
        if perm_check(i) == True:
            print(i)
            solution = True
        else:
            i += 9



Problem_52()

elapsed_time = timeit.timeit(Problem_52, number=10)/10
print(elapsed_time)