# Given n (n >= 3) distinct elements, design two algorithms to compute the first three smallest
# elements using an incremental and a divide-and-conquer approach, respectively. Both your
# algorithms should return a triple (x,y,z) such that x<y<z<(the rest n3input
# elements)and run in linear time in the worst case. Show that your algorithms are correct
# and calculate the exact number of comparisons used by the algorithms. You may assume
# that n=3×2k31 for some positive integer k. Hint: One can use the induction technique
# to show the correctness. Check Chapter 4 for more examples of performance analyses.

import random
import time

def incremental(elements):
    smallestlist = []  # list that will hold the 3 smallest elements
    biggestsmallest = None  # the biggest of the 3 smallest elements

    for i in range(0, len(elements)):  # step through the list incrementally

        if len(smallestlist) < 3:  # fill up the list to begin with
            smallestlist.append(elements[i])
            if biggestsmallest is None or biggestsmallest < elements[i]:
                biggestsmallest = elements[i]  # set biggest element

        elif biggestsmallest > elements[i]:  # if an element smaller than the biggest element in our set of 3 we need to swap
            biggestsmallest = elements[i]  # prematurely set the biggest element to the new one

            for j in range(0,
                           len(smallestlist)):  # step through the smallest element list to find which value needs to go

                if smallestlist[j] > biggestsmallest:
                    biggestsmallest, smallestlist[j] = smallestlist[j], biggestsmallest
    
    for i in range(0,2):
        if smallestlist[i] > smallestlist[i+1]:
            smallestlist[i], smallestlist[i+1] = smallestlist[i+1], smallestlist[i]

    return tuple(smallestlist)

# Median of medians algorithm, used to find the median in a list in worst case linear time
def MoM(elements):

    chunks = []

    # if elements are less than 5 we just take the median
    if len(elements) <= 5:
        elements = sorted(elements)
        return elements[len(elements)//2]

    # divide the elements into chunks of 5, 5 because it's the smallest odd number that allows for linear worst case
    for i in range(0, len(elements), 5):
        # we call recursion to sort since our base case is for elements <= 5
        chunk = elements[i:i+5]
        if len(chunk) == 5:
            if len(chunk) != 0:
                medians = [MoM(chunk)]

    # call median of medians recursively til base case'''
    return MoM(medians)

# Quickselect, used to find the 3 smallest elements only
def QS(elements, k):
    # find a good pivot with median of medians algorithm
    piv = MoM(elements)
    
    # make pointers for left, right and current position
    i = left = 0
    right = len(elements)-1

    # progress the left and right pointer towards eachother
    while left < right:
        # if we find the pivot there is no need to swap places, just progress current pointer to be ahead of the left
        if elements[i] == piv:
            i = i+1
        # if the element at the current pointer is smaller than the pivot we swap them
        # this won't acutally do anything until we've found our pivot as the current pointer is traveling with the left pointer to begin with
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
        return tuple(sorted(elements[:k]))
    # if the "k"th element is ranked lower than left we call recursion on the left side of our elements
    elif k < left:
        return QS(elements[0:left], k)
    # if the "k"th element is ranked higher than left we call recursion on the right side of our elements
    # we also need to take the "k"th place into mind when we choose from this side is the ranks under it are now gone
    else:
        if k >= i:
            return tuple(sorted(elements[:k]))
        return QS(elements[left:len(elements)], k - left)


if __name__ == '__main__':
    randomlist = []
    amountofelems = 3*2**10 # assuming n = 3*2^k as in the lab spec
    randomlist = random.sample(range(0, amountofelems*10), amountofelems)

    randomlist2 = []
    amountofelems = 2**4
    for i in range(0, amountofelems):
        n = random.randint(-amountofelems*10, amountofelems*10)
        randomlist2.append(n)

    #print(randomlist)
    start_time = time.time()
    print("Incremental > ", incremental(randomlist))
    print("it took: ", (time.time()-start_time), "seconds for incr")

    start_time = time.time()
    print("Div and Conq qs > ", QS(randomlist, 3))
    print("it took: ", (time.time()-start_time), "seconds for qs")

    '''print(randomlist2)
    start_time = time.time()
    print(maxSubArrSum(randomlist2))
    print("it took: ", (time.time()-start_time), "seconds for max sum")'''