#The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii)
#each of the 4-digit numbers are permutations of one another.

#There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

#What 12-digit number do you form by concatenating the three terms in this sequence?
from itertools import permutations
import math

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
    for p in range(1000, n): 
        if prime[p]: 
            primes.append(p)
    
Esieve(10000)
test= []
for p in primes:
    b = p+3330
    if b in primes:
        c= p+6660
        if c in primes:
            test.append(p)
for num in test:
    if '0' not in str(num) and num!= 1487:
        b=num+3330
        d=num+6660
        arr1 = list(permutations(str(num)))
        arr2 = []
        arr3 = []
        for a in str(b):
            arr2.append(a)
        for c in str(d):
            arr3.append(c)   
        arr2 = tuple(arr2)
        arr3 = tuple(arr3)
        if arr2 in arr1 and arr3 in arr1:
            print('The answer is',(num*10**8+(num+3330)*10**4+(num+6660)))
            break
    



