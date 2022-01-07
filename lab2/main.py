import random


####################################################################################################
####################################################################################################
# Given n (n >= 3) distinct elements, design two algorithms to compute the first three smallest
# elements using an incremental and a divide-and-conquer approach, respectively. Both your
# algorithms should return a triple (x,y,z) such that x < y < z < (the rest n-3 input
# elements) and run in linear time in the worst case. Show that your algorithms are correct
# and calculate the exact number of comparisons used by the algorithms. You may assume
# that n=3×2k31 for some positive integer k. Hint: One can use the induction technique
# to show the correctness. Check Chapter 4 for more examples of performance analyses.
####################################################################################################
####################################################################################################

def incremental(elements):
    smallestlist = []  # list that will hold the 3 smallest elements
    biggestsmallest = None  # the biggest of the 3 smallest elements

    # Base case k = 0, n = 3
    for i in range(0,3):
        smallestlist.append(elements[i])
        if biggestsmallest is None or biggestsmallest < elements[i]:    # 3
                biggestsmallest = elements[i]  # set biggest element

    for i in range(3, len(elements)):

        if biggestsmallest > elements[i]:  # if an element smaller than the biggest element in our set of 3 we need to swap   n-3
            biggestsmallest = elements[i]  # prematurely set the biggest element to the new one

            for j in range(0,len(smallestlist)):  # step through the smallest element list to find which value needs to go      
                if smallestlist[j] > biggestsmallest:                                                                       #   3
                    biggestsmallest, smallestlist[j] = smallestlist[j], biggestsmallest
    ######### 3*(n-3) #######

    for i in range(0,2): # 9
        for j in range(1,3):
            if smallestlist[i] > smallestlist[j]:
                smallestlist[i], smallestlist[j] = smallestlist[j], smallestlist[i]

    #### 3+3*(n-3)+9 = 12+3*(n-3)

    return tuple(smallestlist)


def divnconq(elements, k=3):
    increment()
    if len(elements) < k:  # +1
        return elements

    left = divnconq(elements[:len(elements) // 2], k)  # +T(n//2)
    right = divnconq(elements[len(elements) // 2:], k)  # +T(n//2)
    smallestelems = incremental(left + right)  # F(n)

    return incremental(smallestelems)


COUNT = 0


def increment():
    global COUNT
    COUNT = COUNT + 1


def reset():
    global COUNT
    COUNT = 0


####################################################################################################
####################################################################################################
# Given an array A=ka1,a2,···,anl of non-zero real numbers, the problem is to nd a
# subarray kai,ai+1,···,aj l (of consecutive elements) such that the sum of all the numbers
# in this subarray is maximum over all possible consecutive subarrays. Design a divide and
# conquer algorithm to compute such a maximum sum. You do not need to actually output
# such a subarray; only returning the maximum sum. Write only one recursive function to
# implement your algorithm. Built-in functions or methods for strings or lists must not be
# used. Your algorithm should run in O(n)time in the worst case. You may assume that
# n=2k for some positive integer k.
####################################################################################################
####################################################################################################


def max_subarray(array):
    # If the array length is 1, we return the only element
    # and assign it to all variables, max left, max right, max sum and total max
    if len(array) == 1:
        return [array[0], array[0], array[0], array[0]]  # all vars in Sum is set to the single elements value
    else:

        # find the middle of the list
        #        ↓ this is the pivot
        # +---+---+---+---+
        # | 1 | 2 | 3 | 4 |
        # +---+---+---+---+
        mid = len(array) // 2

        left_list = array[:mid]
        right_list = array[mid:]

        # +---+---+     +---+---+
        # | 1 | 2 |     | 3 | 4 |
        # +---+---+     +---+---+
        # We split the list
        # into two parts, left and right
        # and recursively call the function on each of them
        left = max_subarray(left_list)
        right = max_subarray(right_list)

        left_max_left = left[0]
        left_max_right = left[1]
        left_total_sum = left[2]
        left_max_sum = left[3]

        right_max_left = right[0]
        right_max_right = right[1]
        right_total_sum = right[2]
        right_max_sum = right[3]

        # Total sum The sum of all elements in the array
        total_sum = left_max_sum + right_max_sum

        # Max left sum
        # The sum of all elements in the left subarray
        # if max sum left side is greater than the sum of all elements in the sub array + right side max left
        if left_max_left > left_total_sum + right_max_left:
            max_left = left_max_left
        else:
            max_left = left_total_sum + right_max_left

        # Max right sum
        # The sum of all elements in the right subarray
        # if max sum right side is greater than the sum of all elements in the sub array + left side max right
        if right_max_right > right_total_sum + left_max_right:
            max_right = right_max_right
        else:
            max_right = right_total_sum + left_max_right

        # Max sum
        # The maximum sum of all possible sub arrays
        # if the max sum left side is greater than the max sum right side
        if (right_max_sum > left_max_sum) and (right_max_sum > left_max_right + right_max_left):
            max_sum = right_max_sum
        elif (left_max_sum > right_max_sum) and (left_max_sum > left_max_right + right_max_left):
            max_sum = left_max_sum
        else:
            max_sum = left_max_right + right_max_left

        # Return an array of all our different variables.
        return [max_left, max_right, total_sum, max_sum]


if __name__ == '__main__':
    randomlist = []

    k = 3 * 2 ** 0
    print('n value: ' + str(k))


    def predictioninc(k):
        return 3 * 2 + 2 + (k - 3) * 3


    def predictiondiv(k):
        return 2 * (k / 2) + 2 * (3 * 2 + 2 + (k - 3) * 3)


    print('prediction increment: ' + str(predictioninc(k)))
    print('prediction divconq: ' + str(predictiondiv(k)))
    for i in range(0, k):
        n = random.randint(1, 100)
        randomlist.append(n)
    # print(randomlist)
    print(incremental(randomlist))
    print(COUNT)
    reset()
    print(divnconq(randomlist))
    print(COUNT)
    reset()
