#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# you really can factor this down to things that go into 20, 19, 18, 17, 16, 15, 14, 13, 12 and 11, because anything else is a factor of a previous
# value 9 into 18 8 into 16 7 into 14 6 into 12 and 5 into 10 into 20 4 into 8,16 or 20 and 3 into 6,9,12,18, etc... 

# from here we know we need to increment by at least 2520
import timeit 

def Problem5():
    x=2520
    Solved = 0
    while Solved == 0:
        x += 2520
        if x % 19 == 0 and x % 18 == 0 and x % 17 == 0 and x % 16 == 0 and x % 15 == 0 and x % 14 == 0 and x % 13 == 0 and x % 12 == 0 and x % 11 == 0:
            print("The answer is:",x)
            Solved = 1 

elapsed_time = timeit.timeit(Problem5, number=10)/10
print(elapsed_time)

