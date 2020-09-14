#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen)
# contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
#ones
ones = [
  len("one"),
  len("two"),
  len("three"),
  len("four"),
  len("five"),
  len("six"),
  len("seven"),
  len("eight"),
  len("nine"),
  len("ten"),
  len("eleven"),
  len("twelve"),
  len("thirteen"),
  len("fourteen"),
  len("fifteen"),
  len("sixteen"),
  len("seventeen"),
  len("eighteen"),
  len("nineteen")
]
#addons
add=[
  len("one"),
  len("two"),
  len("three"),
  len("four"),
  len("five"),
  len("six"),
  len("seven"),
  len("eight"),
  len("nine")
]

# tens
tens = [
  len("twenty"),
  len("thirty"),
  len("forty"),
  len("fifty"),
  len("sixty"),
  len("seventy"),
  len("eighty"),
  len("ninety")
]
# hundreds
hundreds = [
    len("onehundredand"),
    len("twohundredand"),
    len("threehundredand"),
    len("fourhundredand"),
    len("fivehundredand"),
    len("sixhundredand"),
    len("sevenhundredand"),
    len("eighthundredand"),
    len("ninehundredand")
]

#random
random =[
    len("onethousand")
]

#1-99
a=(sum(ones))+(sum(add)*8)+(sum(tens)*10)

#hundreds + 10* 1-99
#-27 accounts for when hundreds are not added to i.e. one hundred is just onehundred not one hundred and
b=((sum(hundreds)*100) -27)+ 10*a

solution = b+sum(random)
print(solution)