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

# median of medians algorithm for finding the 3 smallest elems
def MoM(elements, k):

    # make chunks of 5 elements, 5 because it's the lowest amount of elements while still being odd and linear
    chunks = []
    for i in range(0, len(elements), 5):
        chunks = chunks + [elements[i:i+5]]
    
    # sort chunks
    chunks = [sorted(chunk) for chunk in chunks]

    # now get medians (middle element) of each sorted chunk
    medians = [chunk[len(chunk) // 2] for chunk in chunks]

    # sort the medians and then find the median of the medians (our pivot)
    piv = sorted(medians)[len(medians) // 2]

    # quicksort with out chosen pivot, and use what rank it received in the end
    rank = QS(elements, piv)

    # check if the rank is the targeted rank if so return
    if rank == k:
        return piv
    # if the targeted rank is smaller find new pivot in the half below our pivot and quicksort again
    elif k < rank:
        return MoM(elements[0:rank], k)
    # if the targeted rank is greater find new pivot in the half above our pivot and quicksort again
    else:
        return MoM(elements[rank+1:len(elements)], k - rank - 1)

# quicksort
def QS(elements, piv):
    # make pointers for left, right and current position
    left = 0
    right = len(elements)-1
    i = 0
    
    # loop til left and right pointer connect
    while left < right:
        # if we find the pivot there is no need to swap places
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
    return left

# smallest 3 divide and conquer
def S3DC(elements):
    return (MoM(elements, 0),MoM(elements, 1),MoM(elements, 2))

if __name__ == '__main__':
    randomlist = []
    for i in range(0, 10):
        n = random.randint(1, 100)
        randomlist.append(n)
    print(randomlist)
    print("Incremental > ", incremental(randomlist))
    print("Div and Conq > ", S3DC(randomlist))
