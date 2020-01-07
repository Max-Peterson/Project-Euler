# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 11:30:59 2019

@author: maxp

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""


"""
BRUTE FORCE SOLUTION
"""
test = [2,3,5,7,11,13,17]
answer = []
numbers = [0,1,2,3,4,5,6,7,8,9]
from itertools import permutations
   
pandigital = list(permutations(numbers,10))
    
for x in pandigital:
    print(x)
    for i in range(1,8):
        div = x[i] *100 + x[i+1]*10 + x[i+2]
        if div % test[i-1] != 0 :
            continue
        if div % test[i-1] == 0 and x not in answer:
            answer.append(x)

"""
GOOD SOLUTION
"""

""" 
Assumptions can be made based on the divisory properties explained in lines 
11 - 17 through this analysis the search space of pandigital numbers and in 
this case the answer itself can be devised quickly.
"""
""" 
First, we know that d6 must either be 0 or 5 because d4d5d6 is divisible by 5
Second, we know that d6d7d8 is divisible by 11, if d6 is 0 all combinations 
that satisfy this requirement are non pandigital therefore d6 must be 5. As a 
result d6d7d8 are all 5-- leaving a set of 8 numbers. since d7d8d9 must be 
divisible and d7d8 only has 8 sequences in order to satisfy d7d8d9 there are 
only 4 combinations 5286,5390,5728 and 5832

At the end of this process we arrive at the final 8 numbers have to be either 
30952867, 60357289, and 06357289 since 1 and 4 are excluded and d1 and d2 have 
essentially no rules there is a set of 2 for each of those 3 numbers.
Based on these rules the answer is simply...
"""

answer = [14309528674,4130952867,1460357289,4160357289,1406357289,4106357289]
    
print('The sum of pandigital numbers with the special property is', sum(answer))
