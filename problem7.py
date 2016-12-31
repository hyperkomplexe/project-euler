##Project Euler
##Problem number: 7
##Author: Nick Hall
##Date: 31/12/2016

#Problem is to find the 10001st prime number.
#Every number greater than 1 is either prime, or a multiple of primes.
#Here we keep a list of primes (so it can be used for later projects).
#Keep increasing the number by 2 to test (next_prime), and see if it's evenly
#divisible by all the previously found primes.

#Possible improvements
#It's memory inefficient to keep a large list of numbers.
#next_prime is broadcast across the entire list of primes, so the division is
#done many times. Probably better to loop through the list, and break once
#a the number is found to be evenly divisible.

#Imports
import numpy as np

#Declare variables
prime_list = np.array([2,3])
prime_count = 2
next_prime = 5

#Prime finder loop
while prime_count < 10001:
    if (0 not in next_prime % prime_list):
        prime_list = np.append(prime_list, next_prime)
        prime_count += 1
    next_prime += 2

print("The 10001st prime is: {}".format(prime_list[-1]))
