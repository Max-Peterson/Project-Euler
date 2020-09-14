#The first two consecutive numbers to have two distinct prime factors are:

#14 = 2 × 7
#15 = 3 × 5

#The first three consecutive numbers to have three distinct prime factors are:

#644 = 2² × 7 × 23
#645 = 3 × 5 × 43
#646 = 2 × 17 × 19.

#Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

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

def factor(num):
    fact = []
    for p in primes:
        while num % p == 0:
            fact.append(p)
            num = num/p
        if num == 1:
            if len(np.unique(fact)) == 4:
                return True
            else:
                return False
                

Esieve(40000)

solution = False
num_count = 0 
i = 209 
while solution == False:
    i += 1 
    num = i
    fact = []
    if factor(num) == True:
        num_count += 1
        if num_count == 4:
            print(i-3)
            break
        else: 
            continue
    else: 
        num_count = 0 

   
  


        
