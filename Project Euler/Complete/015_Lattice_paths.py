#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


#How many such routes are there through a 20×20 grid?

import math
#if you had an m by n grid you simply use combinations. in this case 40 directions must be entered each side contributes 20 of the directional
#inputs therefore the math becomes relatively simple...
m=20
n=20

solution = (math.factorial(m+n))/(math.factorial(m)*math.factorial(n))
print(solution)

# However due to the nature of pascal's triangle this formula will function for grids where m != n