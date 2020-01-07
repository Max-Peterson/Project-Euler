#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

#Find the sum of all numbers which are equal to the sum of the factorial of their digits.

#Note: as 1! = 1 and 2! = 2 are not sums they are not included.
import math

numbers=[]
for i in range(200000):
    num = i 
    string = str(i)
    compare = 0
    print(i)
    for c in string:
        integer = math.factorial(int(c))
        compare += integer
        print(integer)
    print(compare)
    if compare == i:
        numbers.append(i)

print(numbers)
        
#while this brute force solution works it takes a long time and there could theoretically be numbers higher than 200000 that solve the problem.
#However, we know this is not the case mathmatically the search space can be simplified to -------. Additionally another time save would be to 
#cache factorials in an array and call them accordingly

factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

numbers=[]
for i in range(200000):
    num = i 
    string = str(i)
    compare = 0
    
    for c in string:
        integer = factorials[int(c)]
        compare += integer
        
    if compare == i:
        numbers.append(i)

print(sum(numbers))