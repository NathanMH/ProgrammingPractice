"""####################
Author: Nathan Mador-House
Title: QuickSort
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
Quick Sort implementation
####################"""

import array_functions as af
import statistics
import sys

###################################################################
# 2. Functions
###################################################################

def get_median(x, y, z):
    return statistics.median([x, y, z])

def quick_sort(array):
    less = []
    equal = []
    more = []
    if len(array) <= 1:
        return array

    pivot = statistics.median([array[0], array[len(array) - 1],  int(len(array))/2])
    for i in array:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            more.append(i)
        else:
            equal.append(i)

    less = quick_sort(less)
    more = quick_sort(more)
    return less + equal + more


###################################################################
# 3. Main
##################################################################

def sort(array):
    return quick_sort(array)

###################################################################
# 4. Testing
###################################################################


