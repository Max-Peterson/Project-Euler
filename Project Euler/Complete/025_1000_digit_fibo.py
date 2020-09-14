#The Fibonacci sequence is defined by the recurrence relation:

#Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# the first 12 terms will be:

#F1 = 1
#F2 = 1
#F3 = 2
#F4 = 3
#F5 = 5
#F6 = 8
#F7 = 13
#F8 = 21
#F9 = 34
#F10 = 55
#F11 = 89
#F12 = 144
#The 12th term, F12, is the first term to contain three digits.

#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
import math

Fibonacci=[1,1]
i=2
term = 0
while len(str(term))< 1000:
    term = Fibonacci[i-2]+Fibonacci[i-1]
    Fibonacci.append(term)
    i +=1
print('the answer is',Fibonacci.index(Fibonacci[-1])+1)




#Pen and Paper
#It is possible to solve this exercise using pen and paper as well, due to the fact that when the Fibonacci numbers 
# become large enough, the Fibonacci numbers converge to
#(golden ration ^n / sqrt(5))>n 

#n in this case is 10^999 to ensure 1000 digits are reached

#now solve the inequality
golden = (1 + 5 ** 0.5) / 2
n = (math.log(10)*999+(math.log(5)/2))/math.log(golden)
n=int(n)
n=n+1
print(n)

#This solution has far superior scaling as it is a single calculation