#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

#How many circular primes are there below one million?
import math
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
    
while x<166666:
    checklow()
    checkhigh()
    x +=1

answer = []
for prime in primes:
    circular=[]
    str_prime = str(prime)
    n = len(str_prime)
    for x in range(n):
        str_prime=str_prime+(str_prime[0])
        str_prime=str_prime[1:]
        print(str_prime)
        circular.append(int(str_prime))
        if int(str_prime) not in primes:
            continue
        
    result =  all(elem in primes  for elem in circular)
    if result:
        answer.append(prime)
    else:
        continue
print(answer)


