#We shall say that an n-digit number is pandigital if it makes use of all the 
#digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is 
#also prime.

#What is the largest n-digit pandigital prime that exists?

#FROM CODE BLOG (https://www.mathblog.dk/project-euler-41-pandigital-prime/)
#  "The trick I learned in 4th grade was that a number is divisible by 3 if and only if the digit sum of the number is divisible by 3. 
#   The digit sum is as the name implies the sum of the digits. We can rather easily find the digit sum of pandigital numbers since we know the digits"

#I found this trick to be inredibly useful as without any testing you know that the pandigital prime must be 7 digits due to the sums of the individual digits
import math
from itertools import permutations
import timeit
numbers = [1,2,3,4,5,6,7]
def is_prime(i):
    if i % 2 != 0 and i % 3 != 0:
        for x in range(5, int(math.sqrt(i))):
            if i % x == 0:
                return False
        return True

Arr = list(permutations(numbers))

def Problem41():
    for i in range (len(Arr)-1,0,-1):
        num = 0 
        for x in range(6,0,-1):
            num += (Arr[i][x]) * 10**(6-x)
        if is_prime(num) == True:
            print('The largest n-digit pandigital prime is',num,)
            break
Problem41()
elapsed_time = timeit.timeit(Problem41, number=10)/10
print(elapsed_time)


