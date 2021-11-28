import random

def incremental(elements):

    smallestlist = []       # list that will hold the 3 smallest elements
    biggestsmallest = None  # the biggest of the 3 smallest elements

    for i in range(0,len(elements)):    # step through the list incrementally

        if len(smallestlist) < 3:       # fill up the list to begin with
            smallestlist.append(elements[i])
            if biggestsmallest is None or biggestsmallest < elements[i]:
                biggestsmallest = elements[i]   # set biggest element

        elif biggestsmallest > elements[i]:     # if an element smaller than the biggest element in our set of 3 we need to swap
            biggestsmallest = elements[i]       # prematurely set the biggest element to the new one

            for j in range(0,len(smallestlist)):    # step through the smallest element list to find which value needs to go

                if smallestlist[j] > biggestsmallest:
                    biggestsmallest, smallestlist[j] = smallestlist[j], biggestsmallest
    
    if smallestlist[0] > smallestlist[1]:
        if smallestlist[1] > smallestlist[2]:
            return [smallestlist[2], smallestlist[1], smallestlist[0]]
        else:
            return [smallestlist[1], smallestlist[0], smallestlist[2]]
    elif smallestlist[1] > smallestlist[2]:
        if smallestlist[2] > smallestlist[0]:
            return [smallestlist[0], smallestlist[2], smallestlist[1]]
        else:
            return [smallestlist[2], smallestlist[0], smallestlist[1]]
    elif smallestlist[2] > smallestlist[0]:
        if smallestlist[0] > smallestlist[1]:
            return [smallestlist[1], smallestlist[0], smallestlist[2]]
        else:
            return smallestlist


if __name__ == '__main__':
    randomlist = []
    for i in range(0,40):
        n = random.randint(1,100)
        randomlist.append(n)
    print(randomlist)
    print(incremental(randomlist))