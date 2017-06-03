"""####################
Author: Nathan Mador-House
Title: Timer
####################"""

#######################
"""####################
Index:
1. Imports and Readme
2. Variables
3. Functions
4. Main
5. Testing
####################"""
#######################

###################################################################
# 1. Imports and Readme
###################################################################
"""####################
A helper function to time simple programs
####################"""

import array_functions as af
import os
import time
import subprocess
import easygui as gui

###################################################################
# 2. Variables
###################################################################

files_list = []
times = []

sorting_algos = ['quick_sort', 'merge_sort', 'insertion_sort', 'selection_sort', 'bubble_sort']

defaults = [10, 10000, 10000]

###################################################################
# 3. Functions
###################################################################

# Run the program with a timer
def run_program_with_timer(sort, number_of_arrays, array_size, array_item_size):
    algo = import_sort_algo(sort)
    arrays = af.make_multiple_arrays(number_of_arrays, array_size, array_item_size)
    for i in arrays:

        # Start timer
        start_time = time.time()
        # Call the program with certain arguments
        algo.sort(i)

        # Calc the time one process took
        process_time = round(time.time() - start_time, 10)
        times.append(process_time)

def get_time_stats(list_of_times):
    total = 0
    worst = list_of_times[0]
    best = list_of_times[0]
    for i in list_of_times:
        if i < best:
            best = i
        elif i > worst:
            worst = i
        total += i
        
    average = round(total/len(list_of_times), 10)
    variance = round(worst - best, 10)
    return round(total, 10), best, worst, average, variance

def print_stats(list_of_times, cycles):
    total, best, worst, average, variance = get_time_stats(times)
    print("-------------------")
    print("Total time:     " + str(total) + " seconds for " + str(cycles) + " cycles.")
    print("Best time:      " + str(best) + " seconds.")
    print("Worst time:     " + str(worst) + " seconds.")
    print("Variance:       " + str(variance) + " seconds.")
    print("Average time:   " + str(average) + " seconds.")
    print("-------------------")

def run_gui():
    directory = get_program_dir_gui()
    program = get_program_gui(get_files_list(directory))
    repetitions = get_number_of_repeats_gui()
    size = get_array_size_gui()
    item_size = get_array_item_size_gui()
    return directory, program, repetitions, size, item_size

def import_sort_algo(program):
    new_import = __import__(program.strip(".py"))
    return new_import

###################################################################
# 4. GUI
###################################################################

# Ask user for the directory location of the program they wish to benchmark
def get_program_dir_gui():
    directory = gui.diropenbox("Navigate to the directory the program is in.", "Created by: Nathan Mador-House")
    return directory + "\\"

# Retrieve the list of files at the location user previously entered
def get_files_list(directory):
    all_files = os.listdir(directory)
    for i in all_files:
        if os.path.isfile(directory + i):
            files_list.append(i)
    return files_list

# Make user select which file they want to benchmark
def get_program_gui(files_list):
    choice = gui.choicebox("Pick the program you would like to benchmark.", "Choose Program", files_list)
    return choice

def get_number_of_repeats_gui():
    repeats = gui.integerbox("How many repetitions would you like to benchmark?", "Repeats", "10", "0", "10001")
    return repeats

def get_array_size_gui():
    array_size = gui.integerbox("What size of array would you like to benchmark?", "Array Size", "10", "0", "1001000")
    return array_size

def get_array_item_size_gui():
    array_size = gui.integerbox("What should the range of values in the arrays be?", "Range of Values", "10", "0", "1001000")
    return array_size

###################################################################
# 5. Main
###################################################################

def main():
    # If not using defaults
    # directory, program, repetitions, array_size, array_item_size = run_gui() 
    # sort = import_sort_algo(program)
    # run_program_with_timer(algo, repetitions, array_size, array_item_size)

    print()
    for i in sorting_algos:
        print(i)
        run_program_with_timer(i, defaults[0], defaults[1], defaults[2])
        print_stats(times, defaults[0])

main()
print()



###################################################################
# 5. Testing
###################################################################





