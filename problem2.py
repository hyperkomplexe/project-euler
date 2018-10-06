##Project Euler
##Problem number: 2
##Author: Nick Hall
##Date: 04/01/2017

#By considering the terms in the Fibonacci sequence whose values do not
#exceed four million, find the sum of the even-valued terms.

#No special method for this, it'll be a brute force.

#Imports
#import numpy as np

#Declarations
fib_sum = 0
fib_num = 1
fib_num_last = 1
fib_num_second_last = 1

#Calculation
while fib_num_last <= 4000000:
    #increment last numbers
    fib_num_second_last = fib_num_last
    fib_num_last = fib_num
    fib_num = fib_num_last + fib_num_second_last
    #sum the even numbers
    if fib_num_last % 2 == 0:
        fib_sum += fib_num_last

print("Sum of even fibonacci numbers below 4 million: {}".format(fib_sum))
