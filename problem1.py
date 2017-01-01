##Project Euler
##Problem number: 7
##Author: Nick Hall
##Date: 01/01/2017


#Find the sum of multiples of 3 and 5 below 1000.

#Using arithmetic series (Gauss).

#Find sum of 3's below 1000 (999)
threes = ((3 + 999) * (999 / 3)) / 2
#Find sum of 5's below 1000 (995)
fives = ((5 + 995) * (995 / 5)) / 2
#Find sum of fives which are also multiples of 3 (multiples of 15)
fifteens = ((15 + 990) * (990 / 15) / 2)
#Add the three's and five's, and subtract the doubles
answer = threes + fives - fifteens

print("The answer is: {}".format(answer))
