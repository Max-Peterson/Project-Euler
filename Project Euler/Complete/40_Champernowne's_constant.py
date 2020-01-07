#An irrational decimal fraction is created by concatenating the positive integers:

#0.123456789101112131415161718192021...

#It can be seen that the 12th digit of the fractional part is 1.

#If dn represents the nth digit of the fractional part, find the value of the following expression.

#d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

import timeit
Numbers = [1,10,100,1000,10000,100000,1000000]
answers=[]
def get(i):
    if i <= 8:
        answers.append(i+1)
    if i > 8 and i <= 188:
        number = int(10+((i-8)/2))
        _index = ((i-8)%2)
        if _index == 0:
            answers.append(int(str(number-1)[-1]))
        else:
            answers.append(int(str(number)[_index-1]))
           
    if i > 188 and i <= 2888:
        number = int(100+((i-188)/3))
        _index = ((i-188)%3)
        if _index == 0:
            answers.append(int(str(number-1)[-1]))
        else:
            answers.append(int(str(number)[_index-1]))

    if i > 2888 and i <=38888:
        number = int(1000+((i-2888)/4))
        _index = ((i-2888)%4)
        if _index ==0:
            answers.append(int(str(number-1)[-1]))
        else: 
            answers.append(int(str(number)[_index-1]))
    if i >38888 and i <=488888:
        number = int(10000+((i-38888)/5))
        _index = ((i-38888)%5)
        if _index == 0: 
            answers.append(int(str(number-1)[-1]))
        else:
            answers.append(int(str(number)[_index-1]))
    if i >488888 and i <=5888888:
        number = int(100000 + ((i-488888)/6))
        _index = ((i-488888)%6)
        if _index == 0:
            answers.append(int(str(number-1)[-1]))
        else:
            answers.append(int(str(number)[_index-1]))
    elif i>5888888:
        print('ERROR','requested value out of known range the final value of the known length of the decimal is ...1000000')

def Problem40():
    for i in Numbers:
        get(i)
    print(answers)
    answer = 0
    for a in answers:
        answer += int(a)
    print(answer)

elapsed_time = timeit.timeit(Problem40, number=1)

print(elapsed_time)
#answer = numbers[0], numbers[9], numbers[99], numbers[999], numbers[9999],numbers[99999],numbers[999999]
#print(answer)
