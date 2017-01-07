##Project Euler
##Problem number: 4
##Author: Nick Hall
##Date: 07/01/2017

#Find the largest palindrome made from the product of two 3-digit numbers.

#Largest 3 digit number is 999
#So just start by multiplying (999 - i) * (999 - j)
#Increase j from 0 to 999 in the first loop
#Increase i from 0 to 999 in the second loop
#And just test for it being a palindromic number at each step

#Imports

#Declerations
num_1 = range(999, 0,-1)
num_2 = range(999, 0,-1)
result = 0

#Count down through the loops
for i in num_1:
    for j in num_2:
        #First found palindrome will be the largest for that value of num_1
        if str(i*j) == str(i*j)[::-1]:
            break
    #see if it's larger than the previously stored palindrome. Overwrite result if it is.
    if i*j > result:
        result = i*j


print("Largest palindrome is: {}".format(result))
