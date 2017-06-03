"""####################
Author: Nathan Mador-House
Title: BubbleSort
####################"""

#######################
"""####################
Index:
1. Imports and Readme
2. Functions
3. Main
4. Testing
####################"""
#######################

###################################################################
# 1. Imports and Readme
###################################################################
"""####################
BubbleSort implementation
####################"""

import array_functions as af

###################################################################
# 2. Functions
###################################################################

def bubble_sort(array):
    swapping = True
    while swapping:
        swapping = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                temp = array[i + 1]
                array[i + 1] = array[i]
                array[i] = temp
                swapping = True
    return array

###################################################################
# 3. Main
###################################################################

def sort(array):
    return bubble_sort(array)

###################################################################
# 4. Testing
###################################################################





