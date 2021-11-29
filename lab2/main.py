# Given n (n >= 3) distinct elements, design two algorithms to compute the first three smallest
# elements using an incremental and a divide-and-conquer approach, respectively. Both your
# algorithms should return a triple (x,y,z) such that x<y<z<(the rest n3input
# elements)and run in linear time in the worst case. Show that your algorithms are correct
# and calculate the exact number of comparisons used by the algorithms. You may assume
# that n=3×2k31 for some positive integer k. Hint: One can use the induction technique
# to show the correctness. Check Chapter 4 for more examples of performance analyses.


import random


def incremental(elements):
    smallestlist = []  # list that will hold the 3 smallest elements
    biggestsmallest = None  # the biggest of the 3 smallest elements

    for i in range(0, len(elements)):  # step through the list incrementally

        if len(smallestlist) < 3:  # fill up the list to begin with
            smallestlist.append(elements[i])
            if biggestsmallest is None or biggestsmallest < elements[i]:
                biggestsmallest = elements[i]  # set biggest element

        elif biggestsmallest > elements[
            i]:  # if an element smaller than the biggest element in our set of 3 we need to swap
            biggestsmallest = elements[i]  # prematurely set the biggest element to the new one

            for j in range(0,
                           len(smallestlist)):  # step through the smallest element list to find which value needs to go

                if smallestlist[j] > biggestsmallest:
                    biggestsmallest, smallestlist[j] = smallestlist[j], biggestsmallest

    if smallestlist[0] > smallestlist[1]:
        if smallestlist[1] > smallestlist[2]:
            return smallestlist[2], smallestlist[1], smallestlist[0]
        else:
            return smallestlist[1], smallestlist[0], smallestlist[2]
    elif smallestlist[1] > smallestlist[2]:
        if smallestlist[2] > smallestlist[0]:
            return smallestlist[0], smallestlist[2], smallestlist[1]
        else:
            return smallestlist[2], smallestlist[0], smallestlist[1]
    elif smallestlist[2] > smallestlist[0]:
        if smallestlist[0] > smallestlist[1]:
            return smallestlist[1], smallestlist[0], smallestlist[2]
        else:
            return tuple(smallestlist)


# Divide and Conquer

def divideAndConquer(elements):
    length = len(elements)
    if length == 1:  # base case since a list of one element is sorted
        return elements
    mid = length // 2
    left = divideAndConquer(elements[:mid])
    right = divideAndConquer(elements[mid:])
    ret = []
    max_value = length if length < 3 else 3
    while len(ret) < max_value and left and right:
        if left[0] < right[0]:
            ret.append(left[0])
            del left[0]
        else:
            ret.append(right[0])
            del right[0]
    if len(ret) < max_value:
        ret.extend(left)
        ret.extend(right)

    return ret


#
# Given an array A=a1,a2,···,an of non-zero real numbers, the problem is to find a
# subarray ai,ai+1,···,aj  (of consecutive elements) such that the sum of all the numbers
# in this subarray is maximum over all possible consecutive subarrays. Design a divide and
# conquer algorithm to compute such a maximum sum. You do not need to actually output
# such a subarray; only returning the maximum sum. Write only one recursive function to
# implement your algorithm. Built-in functions or methods for strings or lists must not be
# used. Your algorithm should run in O(n)time in the worst case. You may assume that
# n=2k for some positive integer k.
#

"""
    

"""
def maxSubArray(lst):
    if len(lst) == 1:
        return lst[0]

    mid = len(lst) // 2

    left = maxSubArray(lst[:mid])
    right = maxSubArray(lst[mid:])

    left_index = 1
    right_index = 0
    left_center = 0
    right_center = 0
    while left_index <= mid and lst[mid - left_index] > 0:
        left_center = left_center + lst[mid - left_index]
        left_index += 1
    while right_index < mid and lst[mid + right_index] > 0:
        right_center = right_center + lst[mid + right_index]
        right_index += 1
    center_sum = right_center + left_center
    if center_sum > right and center_sum > left:
        return center_sum
    elif right > left:
        return right
    else:
        return left


if __name__ == '__main__':
    randomlist = []
    for i in range(0, 40):
        n = random.randint(1, 100)
        randomlist.append(n)

    print(randomlist)
    print(incremental(randomlist))
    print(tuple(divideAndConquer(randomlist)))
    print(maxSubArray(randomlist))
