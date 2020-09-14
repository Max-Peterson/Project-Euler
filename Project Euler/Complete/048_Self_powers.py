#The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

#Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
import timeit
def Problem48():
    answer=0
    for i in range (1,1000):
        number = str(i**i)
        num = number[-10:]
        answer += int(num)

    Response = str(answer)
    print(Response[-10:])

elapsed_time = timeit.timeit(Problem48, number=10)/10
print(elapsed_time)
 
#while this code runs in 43 ms I think this can be improved by using a different way to 
#manipulate the number of digits at each calculation possibly only calculating ten rather 
#than calculating the whole number and then slicing it