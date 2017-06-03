"""####################
Author: Nathan Mador-House
Title: Arrays
####################"""

#######################
"""####################
Index:
1. Imports and Readme
2. General Functions
3. GUI / Visual
4. Testing
####################"""
#######################

###################################################################
# 1. Imports and Readme
###################################################################
"""####################
A bunch of array functions
####################"""

import random
import easygui
import sys

###################################################################
# 2. Functions
###################################################################

def make_array(size, array_item_max):
    array = []
    for i in range(size):
        r = random.randint(1, array_item_max)
        array.append(r)
    return array

def make_multiple_arrays(amount, size, array_item_max):
    arrays = []
    for i in range(amount):
        arrays.append(make_array(size, array_item_max))
    return arrays

def swap_values(val1, val2):
    temp = val1
    val1 = val2
    val2 = temp
    return val1, val2

def print_array(array):
    for i in range(0, len(array)):
        print(str(i) + " : " + str(array[i]))

###################################################################
# 3. GUI / Visual
###################################################################

###################################################################
# 4. Testing
###################################################################


