#There are exactly ten ways of selecting three from five, 12345:
#123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#How many, not necessarily distinct, values of pascal's triangle in the first 100 rows are greater than one-million?


# to get each number in row you simply multiply the previous number (all rows start with 1) by the (row number - term number)/(1+termnumber) assuming the first term after 1 is "0"

#example row 4 is 1 4 6 4 1 that is 1 * (4/1) = 4, 4*(3/2) =6, 6*(2/3) = 4, 4* (1/4) = 1 

# this means that we don't need to cache Pascal's triangle which was previously my intent to improve upon the brute force method. With a cutoff at one million as the result of a term, and utilizing the symmetry of the triangle
#this should produce the most efficient results
count = 0
limit = 1000000
for i in range(3,101,1):
    term = 0
    value = 1
    while value < limit and term < i/2:
        term += 1
        value = value * (i-term+1)/(term)
        
        if value > limit:
            count += (i+1) - 2*(term)
            

print("the number of terms over 1 million in the first 100 rows of Pascal's Triangle is", count)