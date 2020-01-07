#A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

#1/2	= 	0.5
#1/3	= 	0.(3)
#1/4	= 	0.25
#1/5	= 	0.2
#1/6	= 	0.1(6)
#1/7	= 	0.(142857)
#1/8	= 	0.125
#1/9	= 	0.(1)
#1/10	= 	0.1
#Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
#First intuition would tell me that even numbers will not generate a repeating sequence additionally prime numbers are the most likely candidate for 
#time simplification

import math

#Frst, create  a list of primes not divisible by 5 

x=1
primes=[3]

def checklow():
    a = (6*x) -1
    alim = math.sqrt(a)
    if a % 5 == 0:
        return
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
    if b % 5 == 0:
        return
    for p in primes:
        if p <= blim:
            if b % p == 0:
                return
        else:
            primes.append(b)
            return
    
while x<167:
    checklow()
    checkhigh()
    x +=1
print(primes)
print(len(primes))
#Test this list to find the longest recurring decimal and the number associated with it

number = 0
longest = 0
for a in primes:
    p = 1
    while (10 ** p) % a != 1:
        p += 1
    if p > longest:
        number = a 
        longest = p

print('the longest recurring decimal is', longest, 'digits long, created by dividing 1 by',number)