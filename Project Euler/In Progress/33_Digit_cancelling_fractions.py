#he fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

#We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

#There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

#If the product of these four fractions is given in its lowest common terms, find the value of the denominator.


for i in range(11,100):
    for x in range(11,100):
        i2=str(i)
        x2=str(x)
        for c in i2:
            if c in x2:
                i2.remove(c)
                x2.remove(c)
        if i/x == int(i2)/int(x2)
        