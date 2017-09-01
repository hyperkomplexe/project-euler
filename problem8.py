##Project Euler
##Problem number: 8
##Author: Nick Hall
##Date: 13/08/2017

#The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
#
#Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

#Imports
import numpy as np
import pandas as pd

long_number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450

#Convert the number into a numpy array
long_array = [np.array(i) for i in str(long_number)]

#Find where the zeros are
for index, value in enumerate(long_array):
    if value == 0:
        print(index)

#If the zeros are less than 12 indicies apart. Discard anything between these zeros, and create a new array.
##If the zeros are less than 12 indicies apart, then there can't be any number combination which is non-zero.
##
#Create new arrays based on these break points.
zero_found = False
last_zero_index = 0
product_arrays = np.array()

for index, value in enumerate(long_array):
    print(index, value)
    if value == 0:
        if zero_found & (index - last_zero_index <= 13):
            #print(long_array[last_zero_index:index].prod())
            print("Break between long_array[{}] and long_array[{}]".format(last_zero_index, index))

        zero_found = True
        last_zero_index = index

#After each zero found, find the largest multiple of the numbers before it (to the last zero found). And keep only the largest.

def find_largest_product(long_array):
    largest_product = 0
    start_index = 0
    finish_index = 13
    #Bounds testing because it needs to skip 13 along in the array
    if finish_index <= (len(long_array) - 1):
        for i in long_array[start_index:finish_index]:
            if i.prod() > largest_product:
                largest_product = i.prod()
            print(largest_product)
        start_index += 1
        finish_index += 1
