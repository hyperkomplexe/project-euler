##Project Euler
##Problem number: 6
##Author: Nick Hall
##Date: 08/01/2017

#Find the difference between the sum of the squares of the first one
#hundred natural numbers and the square of the sum.

#Imports
import numpy as np

#Declerations
sum_of_squares = 0
square_of_sum = 0

#Using numpy arrays and broadcasting
sum_of_squares = sum(np.arange(1,101)**2)
square_of_sum = sum(np.arange(1,101))**2
print("Brute force answer: {}".format(square_of_sum - sum_of_squares))

#Square of sum. Arethmetic series to add all the values, then square it.
square_of_sum =  (101 * 100 / 2)**2
#Sum of squares. I had to look this one up: (n(n+1)(2n+1))/6
sum_of_squares = (100 * (100 + 1) * ((2 * 100) + 1)) / 6
print("Arethmetic answer: {}".format(square_of_sum - sum_of_squares))


#answer: 25164150
