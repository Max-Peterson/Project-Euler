#It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

#9 = 7 + 2×1^2
#15 = 7 + 2×2^2
#21 = 3 + 2×3^2
#25 = 7 + 2×3^2
#27 = 19 + 2×2^2
#33 = 31 + 2×1^2

#It turns out that the conjecture was false.

#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

#Sieve of Marouane states that all odd composites can be made from p**2 +2*p*c where p is a prime number other than 2 and c is a constant 
#the key to this problem is solving for a the min of the function that does not allow the above equation to be equal to another p added to a square 
import math
import timeit
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
    
def Problem46():
    Esieve(10000)
    odd = 33
    answer = 0
    i=0
    while answer == 0:
        if odd >= primes[i]:
            if math.sqrt((odd - primes[i])/2).is_integer() == True:
                odd+=2
                i=0
            else:
                i += 1
        else:
            answer = 1
            print('The smallest counter example is',odd)
            
elapsed_time = timeit.timeit(Problem46, number=10)/10
print(elapsed_time)

           
    
    
