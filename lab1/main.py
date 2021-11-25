import random
import time
import matplotlib.pyplot as plt


##############################################################################
# The normal merge sort algorithm
# Split each array in half and sort them recursively
# Average and Worse O(n log n) Best case O(n)
##############################################################################
def default_mergeSort(arr):
    if len(arr) > 1:  # If the array is bigger then 1
        mid = len(arr) // 2  # Find the middle element
        left = arr[:mid]  # Get the left half
        right = arr[mid:]  # Get the right half

        default_mergeSort(left)  # Sort the left half

        default_mergeSort(right)  # Sort the right half

        i = j = k = 0  # Initialize the indexes

        while i < len(left) and j < len(right):
            if left[i] < right[j]:  # If the left element is smaller then the right
                arr[k] = left[i]  # Insert the left element
                i += 1  # Increment the left index
            else:
                arr[k] = right[j]  # Insert the right element
                j += 1  # Increment the right index
            k += 1  # Increment the index

        while i < len(left):
            arr[k] = left[i]  # Insert the left elements
            i += 1  # Increment the left index
            k += 1  # Increment the index

        while j < len(right):
            arr[k] = right[j]  # Insert the right elements
            j += 1  # Increment the right index
            k += 1  # Increment the index
    return arr  # Return the sorted array


###############################################################################
# Method to split the list in chunks by a k value
# Then sends the chunks to the inserted algorithm method
###############################################################################
def splitSubList(arr, k, sort_algo):
    chunks = [arr[x:x + k] for x in range(0, len(arr), k)]  # Split the array in chunks of k elements

    if len(chunks) > 1:  # If the array is bigger then k
        while len(chunks) > 1:  # If there are less than 2 chunks
            chunks[0] = sort_algo(chunks[0] + chunks[1])  # Merge the chunks
            chunks.pop(1)  # Remove the second chunk
            if len(chunks) > 2:  # If there are more than 2 chunks
                chunks[len(chunks) - 1] = \
                    sort_algo(chunks[len(chunks) - 1] + chunks[len(chunks) - 2])  # Merge the last 2 chunks
                chunks.pop(len(chunks) - 2)  # Remove the second to last chunk
    else:
        chunks[0] = sort_algo(chunks[0])  # If there is only 1 chunk, sort it

    return chunks[0]  # Return the sorted list


###############################################################################
# Merge Sort with the binary search method
# average O(n log n)
###############################################################################
def b_sort(arr):
    for i in range(1, len(arr)):  # Loop through the array
        temp = arr[i]  # Get our key
        pos = binary_search(arr, temp, 0, i) + 1  # Find its desired position
        for k in range(i, pos, -1):  # Loop though each sorted elements after the new key position
            arr[k] = arr[k - 1]  # Move the sorted elements to the right
        arr[pos] = temp  # Insert the key into the correct position
    return arr  # Return the sorted array


###############################################################################
# Binary search method
###############################################################################
def binary_search(arr, key, start, end):
    if end - start <= 1:  # If the array is only 1 element long
        if key < arr[start]:  # If the key is smaller then the first element
            return start - 1
        else:  # If the key is bigger then the first element
            return start

    mid = (start + end) // 2  # Find the middle element

    if arr[mid] < key:  # If the middle element is smaller then the key
        return binary_search(arr, key, mid, end)
    elif arr[mid] > key:  # if the middle element is bigger then the key
        return binary_search(arr, key, start, mid)
    else:  # Else its the key
        return mid


###############################################################################
# Insertion sort algorithm
# average and worse case O(n^2) best O(n)
###############################################################################
def insertion_sort(array):
    i = 1
    while i < len(array):  # Loop though the array
        j = i
        while j > 0 and array[j - 1] > array[j]:  # If the previous value is smaller then our element
            temp = array[j]  # Put our element in a temp variable
            array[j] = array[j - 1]  # Move the previous element to the right
            array[j - 1] = temp  # Insert the temp variable into the correct position
            j -= 1  # Go to the element to the left
        i = i + 1  # Go to the next element
    return array  # Return the sorted element


###############################################################################
# Different test to calculate times and plot the results
###############################################################################

###############################################################################
# Check runtime for 2 different sorting algorithms
###############################################################################
def runtime2(tests, k):
    time1 = []
    time2 = []
    time3 = []
    size = []
    i = 1
    while i <= tests:
        s = 100 * i
        print(i, '/', tests, '-', s)

        size.append(s)
        _list = [random.randrange(1, 1000, 1) for i in range(s)]

        start = time.time()
        splitSubList(_list, 2, b_sort)
        end = time.time()

        start2 = time.time()
        splitSubList(_list, k, insertion_sort)
        end2 = time.time()

        start3 = time.time()
        splitSubList(_list, k, default_mergeSort)
        end3 = time.time()

        time1.append(end - start)
        time2.append(end2 - start2)
        time3.append(end3 - start3)
        i += 1

    ax = plt.axes()
    ax.plot(size, time1, label=b_sort.__name__)
    ax.plot(size, time2, label=insertion_sort.__name__)
    ax.plot(size, time3, label=default_mergeSort.__name__)
    plt.legend()
    plt.show()


###############################################################################
# Find the best k value for each algorithm
###############################################################################
def findBestK(tests):
    time1 = []
    time2 = []
    k = []
    f = []
    i = 1
    j = 1
    now = time.time()
    while j <= tests:
        _f = 1 * j
        print(j, '/', tests, '-', _f, '(', round(time.time() - now), ')')

        f.append(_f)
        _list = [random.randrange(1, 1000, 1) for i in range(10000)]
        start2 = time.time()
        splitSubList(_list, _f, insertion_sort)
        end2 = time.time()
        time2.append(end2 - start2)
        j += 4

    now = time.time()
    while i <= tests:
        _k = 1 * i
        print(i, '/', tests, '-', _k, '(', round(time.time() - now), ')')

        k.append(_k)
        _list = [random.randrange(1, 1000, 1) for i in range(10000)]

        start = time.time()
        splitSubList(_list, _k, b_sort)
        end = time.time()

        time1.append(end - start)

        i += 4

    ax = plt.axes()
    ax.plot(k, time1, label='k value b_sort')
    ax.plot(f, time2, label='k value insertion_sort')
    plt.title('method as function of k')
    plt.legend()
    plt.show()


###############################################################################
# Generate a plot and showing the different time for different sorting algorithms
# when having different sized inputs and k value
###############################################################################
def compareDifferentInputsAndKValue(tests):
    time1 = []
    time2 = []
    time3 = []
    size = []
    k = []
    i = 1
    j = 1
    while i < tests:
        print(i)
        while j < tests:
            _size = 500 * i
            _k = 50 * j
            print(i, '/', tests, '-', _size, '-', _k)

            _list = [random.randrange(1, 1000, 1) for i in range(_size)]
            start1 = time.time()
            splitSubList(_list, _k, insertion_sort)
            end1 = time.time()
            time1.append(end1 - start1)

            start = time.time()
            splitSubList(_list, _k, b_sort)
            end = time.time()
            time2.append(end - start)

            start = time.time()
            splitSubList(_list, 2, default_mergeSort)
            end = time.time()
            time3.append(end - start)
            j += 1
        j = 1
        i += 1

    ax = plt.axes(projection='3d')
    ax.plot3D(k, size, time1)
    ax.plot3D(k, size, time2)
    ax.plot3D(k, size, time3)
    plt.title('method as function of k')
    plt.legend()
    plt.show()


###############################################################################
# Find point when b_sort does a faster job than insertion method
# Found to be around after 30-50 elements in the list
###############################################################################
def findFasterPoint(tests):
    i = 2
    j = 0
    size = []
    time1 = []
    time2 = []

    while tests > j:
        while True:
            _list = [random.randrange(1, 1000, 1) for i in range(i)]
            start = time.time()
            splitSubList(_list, 400, insertion_sort)
            end = time.time()
            _time1 = end - start

            start = time.time()
            splitSubList(_list, 800, b_sort)
            end = time.time()
            _time2 = end - start

            print(_time2, _time1)
            time1.append(_time1)
            time2.append(_time2)
            size.append(i)
            if _time2 < _time1:
                print('at size:', i)

                break
            i += 1
        j += 1

    def Average(lst):
        return sum(lst) / len(lst)

    print(Average(size))
    ax = plt.axes()
    ax.plot(size, time1, label='insertion_sort')
    ax.plot(size, time2, label='b_sort')
    plt.legend()
    plt.show()


###############################################################################
# Python main function
###############################################################################
if __name__ == '__main__':
    _list = [random.randrange(1, 1000, 1) for i in range(20)]  # 20 random numbers
    j = splitSubList(_list, 800, b_sort)  # Run b-sort
    y = splitSubList(_list, 2, default_mergeSort)  # Run merge sort
    z = splitSubList(_list, 400, insertion_sort)  # Run insertion sort
    print(j)  # Print the result of b-sort
    print(y)  # Print the result of merge sort
    print(z)  # Print the result of insertion sort
