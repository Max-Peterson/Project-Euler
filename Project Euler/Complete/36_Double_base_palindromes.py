#The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

#(Please note that the palindromic number, in either base, may not include leading zeros.)
numbers = []
for i in range(9):
    for x in range (10):
        numbers.append(((i+1) *100)+x*10+(i+1))
more_numbers=[]
for i in range(9):
    for number in numbers:
        more_numbers.append((i+1)*10000 + (number*10) + (i+1))
more_more_numbers = []
for i in range(9):
    for x in range(10):
        more_more_numbers.append((i+1)*1000+(x*110)+(i+1))
more_more_more_numbers = []
for i in range(9):
    for number in more_more_numbers:
        more_more_more_numbers.append((i+1)*100000 + (number*10) + (i+1))
print(numbers)
print(more_numbers)
print(more_more_numbers)
print(more_more_more_numbers)

palindromes = (numbers + more_numbers + more_more_numbers + more_more_more_numbers)
print(palindromes)
answer=[]
for number in palindromes:
    A=str(bin(number))[2:]
    print(A)
    print(A[::-1])
    if A == A[::-1]:
        answer.append(number)
print(answer)