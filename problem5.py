##Project Euler
##Problem number: 5
##Author: Nick Hall
##Date: 13/01/2017

#2520 is the smallest number that can be divided by each of the numbers
#from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all
#of the numbers from 1 to 20?

#Every number is either prime, or a multiple of primes. So this means we find the
#prime factors for each number from 1 to 20.
#Finding the smallest multiple, means taking enough of the factors to re-create
#any of the numbers from 1 to 20.

#Example, primes from 1 to 10 are: 2,3,5,7. Then we make each number from 1 to 10
#as a multiple of these primes.
#2 = 2, 3 = 3, 4 = 2x2, 5 = 5, 6 = 2x3, 7 = 7, 8 = 2x2x2, 9 = 3x3, 10 = 2x5.
#So we just need enough of the prime factors to create any of these.
#2 x 3 x 2 (another 2, because we need two of them to make 4) x 5 x 7 x 2
#(yet another 2 because we need three of them to make 8) x 3 (to make 9).
#2x3x2x5x7x2x3 = 2520

#A result of the above, we can see that the highest number of multiples of any prime
#happens at the highest power of the prime, which the result is still under 20.
#Another example. 2^4 = 16, so we need exactly four 2's in the prime factor list.
#3^2 = 9, so we need exactly two 3's in the prime factor list.
#5^2 = 25, so we're already over on this one. That means for all primes from 5
#to below 20, there will be only one of.
#So the final answer would be: 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19

#So essentially, to program it we start at the first prime and find the highest
#power we can raise it to, before it reaches 20. Then continue along the primes
#until we can only reach a power of 1. Then just include one of the rest of the
#primes under 20.

#It was a long way to get to here, but it seems I don't really need to program a
#solution as it's easier to do by simple logic

print(2 * 2 * 2 * 2 * 3 * 3 * 5 * 7 * 11 * 13 * 17 * 19)

#Answer: 232792560
