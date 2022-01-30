# ShockingRotom June, 2021
## PythonSortingAlgorithms
###### Runs and compares different sorting algorithms as well as runs a searching algorithm

Algorithms are measured by the time it takes to complete them and sometimes in very rare occurrences how much space
it takes up. In this smaller example with only 5000 different integers space really isn't an issue. I imported the
time module in order to track how long each sort takes. As expected the first sort, bubble sort takes an
extremely long time and becomes very clear when making the file 10000+ integers long. The first sort has a time
complexity of n^2 for best and worse case. The second sort, Selection sort isn't much better as it still loops through
the lists multiple times taking a extremely long time as the list of data grows. The third sort, Insertion sort, has
best case time complexity of n which is A HUGE improvement compared to its counterparts above.
