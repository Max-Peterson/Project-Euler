#Euler discovered the remarkable quadratic formula:

#n2+n+41
#It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39.
#However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

#The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79.
#The product of the coefficients, −79 and 1601, is −126479.

#Considering quadratics of the form:

#n2+an+b, where |a|<1000 and |b|≤1000

#where |n| is the modulus/absolute value of n
#e.g. |11|=11 and |−4|=4
#Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for 
#consecutive values of n, starting with n=0.

#While there is an obvious brute force solution checking through all values for a and b however, this is a rather large search space
#the search space can be shrunk by knowing that b must prime and a must be odd 
import numpy as np
import math
x=1
primes=[3,-3]

def checklow():
    a = (6*x) -1
    alim = math.sqrt(a)
    for p in primes:
        if p <= alim:
            if a % p == 0:
                return
        else:
            primes.append(a)
            primes.append(-a)
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
            primes.append(-b)
            return
    
while x<300:
    checklow()
    checkhigh()
    x +=1


options = []
for a in primes:
    if a < 1000 and a > -1000:
        options.append(a)

longest = 0
numbers = []
for a in options:
    print(a)
    for b in options:
        count = 0
        for n in range(100):
            primelist = n**2 + a*n + b
            if primelist in primes:
                count+=1
            else:
                if count > longest:
                    longest = count
                    numbers = [a,b]
                    b+=1
                else:
                    b+=1

print(longest, numbers)