"""####################
Author: Nathan Mador-House
Title: MergeSort
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
Simple mergesort implementation
####################"""

import array_functions as af

###################################################################
# 2. Functions
###################################################################

def mergesort(array):
    if len(array) == 1:
        return array

    h1 = array[0:int(len(array)/2)]
    h2 = array[int(len(array)/2):int(len(array))]
    h1 = mergesort(h1)
    h2 = mergesort(h2)
    return merge(h1, h2)
    
def merge(array1, array2):
    sorted_array = []
    while array1 and array2:
        if array1[0] < array2[0]:
            sorted_array.append(array1[0])
            array1.pop(0)
        else:
            sorted_array.append(array2[0])
            array2.pop(0)
    # If stackB runs out of numbers before stackA
    while array1:
        sorted_array.append(array1[0])
        array1.pop(0)
    # If stackA runs out of numbers before stackB
    while array2:
        sorted_array.append(array2[0])
        array2.pop(0)
    return sorted_array

###################################################################
# 3. Main
###################################################################

def sort(array):
    return mergesort(array)


###################################################################
# 4. Testing
###################################################################


