#Multiples of 3 and 5
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

#intuition would have me believe that simply iterating through multiples and summing them would be an easy brute force method that would 
#prove effective up to the problem statement limit of 1000. However, this method would likely scale poorly to extremely large inputs. Perhaps 
#there are shortcuts in the math to be found...

#5 and 10 
import timeit
def Problem1():
    x = 5
    fives = 0
    while x < 1000:
        fives += x
        x += 5
        print(x)
        print(fives)

    y=3
    threes = 0
    while y <= 999:
        if y % 15 == 0:
            y+=3
        else:
            threes += y
            y += 3
            

    total = threes + fives
    print(total)


#alternatively one can use a single interation through the digits by using an OR and iterating through each digit this method although also 
#brute force is still a massive run time efficiency improvement

def Problem1_v2():
    sum1=0
    for i in range (999):
        if i%3 ==0 or i % 5 == 0:
            sum1 += i




#alternatively the use of the formula ∑k=1/2n(n+1). will allow for a few simple math calculations rather than an iterative process and thus 
#not scaling at runtime according to n other than byte size whereas this  previous strategy certainly has nth order scaling. However, it must be 
#remembered that multiples of 15 are counted twice as they are multiples of both 3 and 5 and that is accounted for in the third term of the following

def Dividesum(n,p):
    return n*(p/n)*((p/n)+1)/2

def Problem1_v3():
    result = Dividesum(3,999)+Dividesum(5,999)-Dividesum(15,999)
    print(result)

 



elapsed_time = timeit.timeit(Problem1, number=10)/10
elapsed_time_v2 = timeit.timeit(Problem1_v2, number = 10)/10
elapsed_time_v3 = timeit.timeit(Problem1_v3, number = 10)/10
print(elapsed_time)
print(elapsed_time_v2)
print(elapsed_time_v3)