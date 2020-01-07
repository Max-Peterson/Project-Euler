#The prime 41, can be written as the sum of six consecutive primes:

#41 = 2 + 3 + 5 + 7 + 11 + 13
#This is the longest sum of consecutive primes that adds to a prime below one-hundred.

#The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

#Which prime, below one-million, can be written as the sum of the most consecutive primes?
import math
primes = [0]
primesum = [0]
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
            primesum.append(primesum[-1]+p)
        elif primesum[-1] > 1000000:
            break
 
def is_prime(n):
    for i in range(2,int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

def Problem50():
    answer = 0 
    for x in range(2,8):
        for i in range(1,len(primesum)-x):
            test = len(primesum) -x - i
            if is_prime(primesum[-x] - primesum[i]) == True and test > answer:
                answer = test
                print(answer)
                print(primesum[i])
                print(primesum[-x])
                

           

Esieve(1000000)
Problem50()

            
        
        


        


