#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

#A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 
#can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant 
#numbers is less than this limit.

#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import math
import timeit
import numpy as np

primes = []
def Esieve(n): 
    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
      
    # Print all prime numbers 
    for p in range(2, n): 
        if prime[p]: 
            primes.append(p)

def factor(i):
    fact = []
    num = i 
    for p in primes:
        while num % p == 0:
            fact.append(p)
            num = num/p
        if num == 1:
            if sum fact == 4:
                return True
            else:
                return False