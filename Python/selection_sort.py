"""####################
Author: Nathan Mador-House
Title: SelectionSort
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
Selection Sort implementation
####################"""

import array_functions as af

###################################################################
# 2. Functions
###################################################################

def selection_sort(array):
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index= j

        if min_index!= i:
            array[i], array[min_index] = af.swap_values(array[i], array[min_index])
    return array

###################################################################
# 3. Main
###################################################################

def sort(array):
    return selection_sort(array)

###################################################################
# 4. Testing
###################################################################


