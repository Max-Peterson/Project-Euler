#10001st prime
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?
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
    

while len(primes)<10001:
    checklow()
    checkhigh()
    x +=1
    
print("The 10001st prime number is",primes[10000])




