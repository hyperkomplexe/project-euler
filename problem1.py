##Project Euler
##Problem number: 7
##Author: Nick Hall
##Date: 31/12/2016


#Find the sum of multiples of 3 and 5 below 1000.

#Using geometric series (Gauss).

#Find sum of 3's below 1000 (999)
threes = ((3 + 999) * (999 / 3)) / 2
#Find sum of 5's below 1000 (995)
fives = ((5 + 995) * (995 / 5)) / 2
#Find sum of fives which are also multiples of 3
doubles = 0
#Add the three's and five's, and subtract the doubles
answer = threes + fives - doubles
