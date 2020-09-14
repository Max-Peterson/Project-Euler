#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numb

def palindrome(e):
    Number = e
    Reverse = 0    
    while(Number > 0):    
        Reminder = Number %10    
        Reverse = (Reverse *10) + Reminder    
        Number = Number //10  
        if Reverse == Number:
            array.append(e)
            xarray.append(x)
            yarray.append(y)

xarray = []
yarray = []
array = []
b=999
d=999
for a in range (899):
    x=b-a
    for c in range(899):
        y=d-c
        palindrome(x*y)
value = array.index(max(array))
print(max(array), "is the largest palindrome and the product of", xarray[value],"and", yarray[value])