#The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so 
#the first ten triangle numbers are:

#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

#By converting each letter in a word to a number corresponding to its 
#alphabetical position and adding these values we form a word value. For 
#example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value 
#is a triangle number then we shall call the word a triangle word.

#Using words.txt (right click and 'Save Link/Target As...'), a 16K text file 
#containing nearly two-thousand common English words, how many are triangle 
#words?
import timeit
import ast
import math
def Problem42():
    file2 = open("C:/Users/maxp/OneDrive/Documents/SDE/Project Euler/Complete/42_words.txt")
    A=ast.literal_eval(file2.read())
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O' , 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    answer=[]
    for c in A:
        sum=0
        for letter in c:
            letter = letters.index(letter) + 1
            sum+=letter
        answer.append(sum)
    words = []
    triangle = [1,3,6,10,15,21,28,36,45,55,66,78,91,105,120,136,153,171,190]
    for x in answer:
        if x in triangle:
            words.append(A[answer.index(x)])
    print('There are',len(words),'triangle words')

elapsed_time = timeit.timeit(Problem42, number=10)/10
print(elapsed_time)

#it would be possible to speed this code up if only slightly by calculating the inverse of the triangle number function and performing it on the sums of words
#if the result is a whole number the number is a triangle number rather than comparing to an array of triangle numbers that cover the range of sum values in the 
#text file. After switching the function to do so, the time save was ~2ms but it may be more substantial for a larger set of words.

