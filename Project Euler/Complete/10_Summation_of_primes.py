#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

import math

x=1
primes=[2,3]

def checklow():
    a = (6*x) -1
    alim = math.sqrt(a)
    for p in primes:
        if p <= alim:
            if a % p == 0:
                return
        else:
            primes.append(a)
            return

def checkhigh():
    b = (6*x) +1
    blim = math.sqrt(b)
    for p in primes:
        if p <= blim:
            if b % p == 0:
                return
        else:
            primes.append(b)
            return
    

while primes[-1]< 2000000:
    checklow()
    checkhigh()
    x += 1
    
primes.pop(-1)
print("The sum of all primes below 2,000,000 is",sum(primes))
