#n! means n × (n − 1) × ... × 3 × 2 × 1

#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

#Find the sum of the digits in the number 100!

import math
import timeit
def Problem20():
    n = 100
    print(sum(map(int, str(math.factorial(n)))))

elapsed_time = timeit.timeit(Problem20, number=10)/10
print(elapsed_time)

#There seems to be buzz about estimating the length of the factorial and then using number 
#theory to reduce search space (any positive number with its own sum subtracted from it is a multiple of 9)
#However, this method is still theoretical as there is no way to further reduce search space from in this case 158 possibilities