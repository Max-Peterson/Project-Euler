#A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
#If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
#The lexicographic permutations of 0, 1 and 2 are:

#012   021   102   120   201   210

#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from itertools import permutations
def brute():
    numbers = [0,1,2,3,4,5,6,7,8,9]
    lex_numbers = list(permutations(numbers,9))
    print(lex_numbers[999999])

def elegant():
    numbers = [0,1,2,3,4,5,6,7,8,9]
    answer = []
    divisor = 999999
    fac = [362880,40320,5040,720,120,24,6,2,1,1]
    for i in fac:
        answer.append(numbers[int(divisor/i)])
        numbers.pop(int(divisor/i))
        divisor = divisor % i
    print(answer)

elegant()
