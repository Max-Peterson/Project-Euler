#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

#The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

#HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

# wiht some simple tests it can be verifiedthat the first product must be two digits and the second must be at least three
from itertools import permutations
values = [1,2,3,4,5,6,7,8,9]

    # a * b = C

for i in range(9):
    for x in range(9):
        values = [1,2,3,4,5,6,7,8,9]
        if x==i:
            x+=1
        print(values[i])
        print(values[x])
        a=values[i]*10 + values[x]
    
        values.remove(values[i])
        values.remove(values[x-1])
        newset=values
        b = list(permutations(values,3))
        for e in b:
            answer = [1,2,3,4,5,6,7,8,9]
            b_number = e[0]*100 +e[1]*10 +e[2]
            c = a*b_number
            answer.remove(answer[i])
            answer.remove(answer[x-1])
            answer.remove(e[0])
            answer.remove(e[1])
            answer.remove(e[2])
            c_list=[(int(d) for d in str(c))]
            if c_list.sort() == answer:
                print(a,b_number,c)
        



