# Sorting Algorithms
# June, 2021
# ShockingRotom

# Algorithms are measured by the time it takes to complete them and sometimes in very rare occurrences how much space
# it takes up. In this smaller example with only 5000 different integers space really isn't an issue. I imported the
# time module in order to track how long each sort takes. As expected the first sort, bubble sort takes an
# extremely long time and becomes very clear when making the file 10000+ integers long. The first sort has a time
# complexity of n^2 for best and worse case. The second sort, Selection sort isn't much better as it still loops through
# the lists multiple times taking a extremely long time as the list of data grows. The third sort, Insertion sort, has
# best case time complexity of n which is A HUGE improvement compared to its counterparts above.

# Importing
import random
import time


# Create file
def create_file():
    # Opens file/creates it if it doesnt exist
    f = open('Numbers.txt', 'w')

    # Loops through x amount of times where x represents the amount of integers in the file
    for n in range(5000):
        # Writes a random int from -10000 to 10000
        f.write(str(random.randrange(-10000, 10000)) + '\n')
    # Closes file and returns the file name in this case Numbers.txt
    f.close()
    return 'Numbers.txt'


# Create list
def create_list(file):
    # opens file and stores it in f
    with open(file) as f:
        # Make list of numbers on each line
        f_list = f.readlines()
        # Strip the numbers and make them type integer
        f_list = [int(n.strip()) for n in f_list]
    return f_list


# Swap sort
def bubble_sort(f_list):
    # Start_time used for determining how many seconds it takes to preform this sorting algorithm
    start_time = time.time()
    print("--- Bubble Sort ---")
    # Loops through the length of list ^2
    for i in range(len(f_list)):
        for h in range(len(f_list) - 1):
            # If h is larger than the int to its right then swap them
            if f_list[h] > f_list[h+1]:
                f_list[h], f_list[h+1] = f_list[h+1], f_list[h]
    # Subtracts start time from current time to determine the time that has passes
    end_time = time.time() - start_time
    return f_list, end_time


# Selection sort
def selection_sort(f_list):
    # Start_time used for determining how many seconds it takes to preform this sorting algorithm
    start_time = time.time()
    print("--- Selection Sort ---")
    # Loops through the length of list
    for i in range(len(f_list)):
        # Creates var to keep track of the smallest value in unsorted part of list
        min_pos = i
        # Loops through the list from i + 1 to the end of list (loops through the unsorted part of list)
        for h in range(i + 1, len(f_list)):
            # If the current value is smaller than min_pos make it the new min pos
            if f_list[h] < f_list[min_pos]:
                min_pos = h
        # After loop complete swap the smallest number with i
        f_list[min_pos], f_list[i] = f_list[i], f_list[min_pos]
    # Subtracts start time from current time to determine the time that has passes
    end_time = time.time() - start_time
    return f_list, end_time


# Insertion sort
def insertion_sort(f_list):
    # Start_time used for determining how many seconds it takes to preform this sorting algorithm
    start_time = time.time()
    print("--- Insertion Sort ---")
    for i in range(1, len(f_list)):
        # Key value is the current value of f_list[i]
        key_value = f_list[i]
        # Scan pos is 1 less than the current i or int we are on
        scan_pos = i - 1
        # Loops aslong as scan pos isnt below 0 and scan pos int in the list is larger than the key value
        while (scan_pos >= 0) and (f_list[scan_pos] > key_value):
            # Swap scan pos with the number to its right
            f_list[scan_pos + 1] = f_list[scan_pos]
            scan_pos -= 1
        f_list[scan_pos + 1] = key_value
    # Subtracts start time from current time to determine the time that has passes
    end_time = time.time() - start_time
    return f_list, end_time


# Even numbers search
def even_numbers_search(f_list):
    print("--- Even Numbers Search ---")
    even_numbers = []
    for n in f_list:
        if n % 2 == 0:
            even_numbers.append(n)
    return even_numbers


# Odd numbers search
def odd_numbers_search(f_list):
    print("--- Odd Numbers Search ---")
    odd_numbers = []
    for n in f_list:
        if n % 2 != 0:
            odd_numbers.append(n)
    return odd_numbers


# Positive numbers search
def pos_numbers_search(f_list):
    print("--- Positive Numbers Search ---")
    pos_numbers = []
    for n in f_list:
        if n > 0:
            pos_numbers.append(n)
    return pos_numbers


# Negative numbers search
def neg_numbers_search(f_list):
    print("--- Negative Numbers Search ---")
    neg_numbers = []
    for n in f_list:
        if n < 0:
            neg_numbers.append(n)
    return neg_numbers


# Calling functions and printing data
file = create_file()
num_list = create_list(file)
print("--- Unsorted List ---")
print(num_list)
print("")

bubble_sort_list, end_time = bubble_sort(num_list)
print(bubble_sort_list)
print("It took " + str(end_time) + " seconds to sort")
print("")

selection_sort_list, end_time = selection_sort(num_list)
print(selection_sort_list)
print("It took " + str(end_time) + " seconds to sort")
print("")

insertion_sort_list, end_time = insertion_sort(num_list)
print(insertion_sort_list)
print("It took " + str(end_time) + " seconds to sort")
print("")

even_numbers = even_numbers_search(bubble_sort_list)
print(even_numbers)
print("")

odd_numbers = odd_numbers_search(selection_sort_list)
print(odd_numbers)
print("")

pos_numbers = pos_numbers_search(insertion_sort_list)
print(pos_numbers)
print("")

neg_numbers = neg_numbers_search(insertion_sort_list)
print(neg_numbers)
print("")
