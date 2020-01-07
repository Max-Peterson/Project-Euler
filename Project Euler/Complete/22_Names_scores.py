#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

#For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

#What is the total of all the name scores in the file?

#While there are sorting algorithms, the builtin sort function seems to operate at ideal speed when compared to things like bubble sort and it performes
#identically to merge sort according to forums
#as a result there isn't a ton of optimization ot perform perhaps at incredibly large samples there could be some study of how many instances of names starting with each letter
#along with common/epected names could perform some sort of estimate

#However, these methods are far off and needlessly complex, the only other thing would be to cache names but this list seems to be comprised of unique names...
import ast
import numpy as np

file2 = open('C:/Users/maxp/OneDrive/Documents/SDE/Project Euler/Complete/22_names.txt')
A=ast.literal_eval(file2.read())
A.sort()
print(A)
print(len(A))
i=-1
sumlist=np.zeros((len(A)), dtype=int)
print(sumlist)
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
while i < len(A)-1:
    i+=1
    print(i)
    for c in A[i]:
        sumlist[i] += (letters.index(c)+1)

print(sumlist)
a = 0
while a < len(sumlist):
    sumlist[a] = sumlist[a] * (a+1)
    a+=1
print(sum(sumlist))
           
    
    



