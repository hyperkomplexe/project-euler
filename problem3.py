##Project Euler
##Problem number: 3
##Author: Nick Hall
##Date: 04/01/2017

#What is the largest prime factor of the number 600851475143 ?

#Using fundamental therom of arithmetic
#Every number is either prime or a multiple of primes.
#So finding the largest prime factor just means

#Imports
#import numpy as np

#Declare variables
prime_list = np.array([2,3])
prime_count = 2
next_prime = 5

#Prime finder loop
while prime_count < 100000:
    if (0 not in next_prime % prime_list):
        prime_list = np.append(prime_list, next_prime)
        prime_count += 1
    next_prime += 2

print("The 10001st prime is: {}".format(prime_list[-1]))
