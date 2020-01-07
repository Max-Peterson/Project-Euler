#Take the number 192 and multiply it by each of 1, 2, and 3:

#192 × 1 = 192
#192 × 2 = 384
#192 × 3 = 576
#By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

#The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

#What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

import timeit

def Problem38():
    answer = 0
    
    key = [1,2,3,4,5,6,7,8,9]
    for x in range (9234,9487):
        number = 100002 * x
        magic = lambda num: map(int, str(num))
        test = list(magic(number))
        test.sort()
        if test == key and number > answer:
            answer = number

    print(answer)


elapsed_time = timeit.timeit(Problem38, number=1)

print(elapsed_time)