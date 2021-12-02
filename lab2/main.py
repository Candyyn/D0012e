# Given n (n >= 3) distinct elements, design two algorithms to compute the first three smallest
# elements using an incremental and a divide-and-conquer approach, respectively. Both your
# algorithms should return a triple (x,y,z) such that x<y<z<(the rest n3input
# elements)and run in linear time in the worst case. Show that your algorithms are correct
# and calculate the exact number of comparisons used by the algorithms. You may assume
# that n=3×2k31 for some positive integer k. Hint: One can use the induction technique
# to show the correctness. Check Chapter 4 for more examples of performance analyses.

import random
import time
import matplotlib.pyplot as plt


def incremental(elements):
    smallestlist = []  # list that will hold the 3 smallest elements
    biggestsmallest = None  # the biggest of the 3 smallest elements

    # loop through the elements and find the smallest 3
    for i in range(0, len(elements)):  # step through the list incrementally
        if len(smallestlist) < 3:  # fill up the list to begin with
            smallestlist.append(elements[i])
            if biggestsmallest is None or biggestsmallest < elements[i]:
                biggestsmallest = elements[i]  # set biggest element
        # if an element smaller than the biggest element in our set of 3 we need to swap
        elif biggestsmallest > elements[i]:
            biggestsmallest = elements[i]  # prematurely set the biggest element to the new one

            for j in range(0,
                           len(smallestlist)):  # step through the smallest element list to find which value needs to go

                if smallestlist[j] > biggestsmallest:
                    biggestsmallest, smallestlist[j] = smallestlist[j], biggestsmallest

    for i in range(0, 2):
        if smallestlist[i] > smallestlist[i + 1]:
            smallestlist[i], smallestlist[i + 1] = smallestlist[i + 1], smallestlist[i]

    return tuple(smallestlist)


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


# Median of medians algorithm, used to find the median in a list in worst case linear time
def MoM(elements):
    chunks = []

    # if elements are less than 5 we just take the median
    if len(elements) <= 5:
        elements = default_mergeSort(elements)
        return elements[len(elements) // 2]

    medians = []
    # divide the elements into chunks of 5, 5 because it's the smallest odd number that allows for linear worst case
    for i in range(0, len(elements), 5):
        # we call recursion to sort since our base case is for elements <= 5
        chunk = elements[i:i + 5]
        median = -1
        if len(chunk) == 5:
            if len(chunk) != 0:
                median = MoM(chunk)
        medians = medians + [median]

    # call median of medians recursively til base case'''
    return MoM(medians)


# Quickselect, used to find the 3 smallest elements only
def QS(elements, k):
    # find a good pivot with median of medians algorithm
    piv = MoM(elements)

    # make pointers for left, right and current position
    i = left = 0
    right = len(elements) - 1

    # progress the left and right pointer towards each other
    while left < right:
        # if we find the pivot there is no need to swap places, just progress current pointer to be ahead of the left
        if elements[i] == piv:
            i = i + 1
        # if the element at the current pointer is smaller than the pivot we swap them this won't acutally do
        # anything until we've found our pivot as the current pointer is traveling with the left pointer to begin with
        elif elements[i] < piv:
            elements[left], elements[i] = elements[i], elements[left]
            left += 1
            i += 1
        # if the element at the current pointer is larger than the pivot we swap with the right pointer
        else:
            elements[right], elements[i] = elements[i], elements[right]
            right -= 1

    # left/right is going to be the index position our pivot received after the quickselect algorithm
    # if the rank of the pivot is the withing the ranks 1-3 we return our
    if k == left:
        a = elements[:k][0]
        b = elements[:k][1]
        c = elements[:k][2]

        if a > b:
            a, b = b, a
        if a > c:
            a, c = c, a
        if b > c:
            b, c = c, b

        return a, b, c
    # if the "k"th element is ranked lower than left we call recursion on the left side of our elements
    elif k < left:
        return QS(elements[0:left], k)
    # if the "k"th element is ranked higher than left we call recursion on the right side of our elements
    # we also need to take the "k"th place into mind when we choose from this side is the ranks under it are now gone
    else:
        if k >= i and len(elements[:k]) > 2:
            a = elements[:k][0]
            b = elements[:k][1]
            c = elements[:k][2]

            if a > b:
                a, b = b, a
            if a > c:
                a, c = c, a
            if b > c:
                b, c = c, b

            return a, b, c
        return QS(elements[left:len(elements)], k - left)


# Given an array A=ka1,a2,···,anl of non-zero real numbers, the problem is to nd a
# subarray kai,ai+1,···,aj l (of consecutive elements) such that the sum of all the numbers
# in this subarray is maximum over all possible consecutive subarrays. Design a divide and
# conquer algorithm to compute such a maximum sum. You do not need to actually output
# such a subarray; only returning the maximum sum. Write only one recursive function to
# implement your algorithm. Built-in functions or methods for strings or lists must not be
# used. Your algorithm should run in O(n)time in the worst case. You may assume that
# n=2k for some positive integer k.

def max_subarray(A, i, j):
    # base case
    if i == j:
        return A[i]

    # find the middle of the array
    mid = (i + j) // 2
    # find the maximum sum of the left subarray
    max_left = max_subarray(A, i, mid)

    # find the maximum sum of the right subarray
    max_right = max_subarray(A, mid + 1, j)

    # find the maximum sum of the crossing subarray
    max_cross = max_crossing_subarray(A, i, mid, j)

    # return the maximum of the three
    return max(max_left, max_right, max_cross)


def max_crossing_subarray(A, i, mid, j):
    # find the maximum sum of the crossing subarray
    max_left = -float('inf')

    sum = 0
    # find the maximum sum of the left subarray
    for k in range(mid, i - 1, -1):
        # add the current element to the sum
        sum += A[k]
        # if thpdate it
        if sum > max_left:
            # update the max left
            max_left = sum

    # find the maximum sum of the right subarray
    max_right = -float('inf')
    sum = 0

    for k in range(mid + 1, j + 1):
        # add the current element to the sum
        sum += A[k]
        # if the sum is greater than the current max right we update it
        if sum > max_right:
            # update the max right
            max_right = sum

    # return the maximum of the three
    return max_left + max_right


if __name__ == '__main__':

    x1 = []
    y1 = []

    x2 = []
    y2 = []

    amountofTest = 14
    for i in range(1, amountofTest):
        print(i)
        randomlist = []
        amountofelems = 3 * 2 ** i  # assuming n = 3*2^k as in the lab spec
        randomlist = random.sample(range(0, amountofelems * 10), amountofelems)
        start_time = time.time()
        print(incremental(randomlist))
        y1.append(time.time() - start_time)
        x1.append(amountofelems)

        start_time = time.time()
        print(QS(randomlist, 3))
        y2.append(time.time() - start_time)
        x2.append(amountofelems)

    ax = plt.axes()
    ax.plot(x1, y1, label="Incremental")
    ax.plot(x2, y2, label="Div and Conq qs")

    # naming the x axis
    plt.xlabel('Length of list')
    # naming the y axis
    plt.ylabel('Time (s)')

    # giving a title to my graph
    plt.title('Find the 3 Smallest Value (Incremental)')
    plt.legend()
    # function to show the plot
    plt.show()

    randomlist2 = []
    amountofelems = 2 ** 4
    for i in range(0, amountofelems):
        n = random.randint(-amountofelems * 10, amountofelems * 10)
        randomlist2.append(n)

    print(max_subarray(randomlist2, 0, len(randomlist2) - 1))
