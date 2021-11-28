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


if __name__ == '__main__':
    randomlist = []
    for i in range(0, 40):
        n = random.randint(1, 100)
        randomlist.append(n)
    print(randomlist)
    print(incremental(randomlist))
