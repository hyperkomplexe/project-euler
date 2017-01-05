##Project Euler
##Problem number: 3
##Author: Nick Hall
##Date: 04/01/2017

#What is the largest prime factor of the number 600851475143 ?

#Using fundamental therom of arithmetic
#Every number is either prime or a multiple of primes.
#So finding the largest prime factor just means breaking down the factors
#as much as possible until they reach the primes, and taking the largest.


#Declare variables
number_to_test = 600851475143
prime_factor = number_to_test
divisor = 2
result = 0 #not so neat, but needed because divisor gets written over as 2 on the last calculation

#Find factors, smallest will always be prime
#Checks if the factor is evenly divisible by an odd number (divisor).
#If divisble then use the remainder as the new number to test, and restart the divisor variable.
while prime_factor > 1:
    if prime_factor % divisor == 0:
        prime_factor = prime_factor // divisor
        result = divisor
        divisor = 2
    else:
        ##increase by 2 (unless already 2)
        if divisor == 2:
            divisor += 1
        else:
            divisor += 2

print("Largest prime factor is: {}".format(result))

##Output
##Largest prime factor is: 6857
##[Finished in 0.035s]
