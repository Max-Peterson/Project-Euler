#You are given the following information, but you may prefer to do some research for yourself.

#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

#You could brute force a method that simply iterates through each day increasing the day count by one and counting all times the date alligns 
#accroding to the problem. 

#interestingly, because the sample size is so large (100 years means 1200 months) one can assume a relatively equal distribution of days of the 
#week falling on a specific day

#with this logic the solution is simply 1200/7 =171.4 

#171 is the correct answer 

#In this problem the larger the sample size taken i.e. extending the year range actually simplifies the problem. In the case of smaller ranges 
#more specificity would be required to solve the problem. However, if this were the case then a simple iterative loop would more than suffice 
#in terms of run time

