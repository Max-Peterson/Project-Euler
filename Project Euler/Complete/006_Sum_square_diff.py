#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
import timeit

def Problem6():
    sum_sq = 0
    for x in range (101):
        sum_sq += (x*x)
    sq_sum = ((100*101)/2)*((100*101)/2)
    answer = (sq_sum) - (sum_sq)
    print(answer)



elapsed_time = timeit.timeit(Problem6, number=10)/10
print(elapsed_time)


#at low n values < 10m this equation will work fast enough however as it doesn't scale incredibly well a better subsitution would be to use the arithmatic substitutions
def Problem6improved():
    n=100
    sum_sq2 = (n*(n+1)*((2*n)+1)) / 6
    print(sum_sq2)
    sq_sum2 = ((n*(n+1))/2)*((n*(n+1))/2)
    print(sq_sum2)
    answer = (sq_sum2)-(sum_sq2)
    print(answer)

elapsed_time2 = timeit.timeit(Problem6improved, number=10)/10
print(elapsed_time2)
