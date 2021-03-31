# Uses python3
import sys
import random

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def partition3(a, l, r):
    """The goal in this problem is to redesign a given implementation of the random-ized quick sort
    algorithm so that it works fast even on sequences containing many equal elements.
    To force the given implementation of the quick sort algorithm to efficiently process sequences 
    with few unique elements, your goal is replace a 2-way partition with a 3-way partition. 
    That is, your new partition procedure should partition the array into three parts: < 𝑥 part, 
    = 𝑥 part, and > 𝑥 part.
    
    Input Format 
    The first line of the input contains an integer 𝑛 
    The next line contains a sequence of 𝑛 integers 𝑎0, 𝑎1, . . . , 𝑎𝑛−1

    Constraints
    1 ≤ 𝑛 ≤ 10^5
    1 ≤ 𝑎𝑖 ≤ 10^9 for all 0 ≤ 𝑖 < 𝑛

    Output Format
    Output this sequence sorted in non-decreasing order."""

    print(a)
    print('sorting', a[l:r + 1])

    x = a[l]  # select pivot element (for comparision)

    # point to pivot
    j = l

    # iterate through (sub) array
    for i in range(l + 1, r + 1):
        print("looking at", a[i])
        if a[i] < x:
            # element is <= pivot --> swap with the end of the left half of sub-array
            # (ignoring the pivot and any previously swapped elements)
            j += 1  # extend the left half
            print("swap {} and {}".format(a[i], a[j]))
            a[i], a[j] = a[j], a[i]  # swap

        elif a[i] == x:
            # swap a[i] to start of left half
            print("swap {} and {}".format(a[i], a[j]))
            a[i], a[j] = a[j], a[i]
            j += 1

            # swap the (temp out of place) element back to end of left half
            a[i], a[j] = a[j], a[i]
            print("swap {} and {}".format(a[i], a[j]))
        print(a[l:r+1])
    # swap any elements not the same (i.e. strictly <) as pivot with start of sub-array
    print("half-sorted", a[l:r + 1])
    k = l  # point k to start of sub-array i.e. pivot

    equal_x = 0

    for i in range(l, j + 1):

        if a[i] == x:
            equal_x += 1

    for i in range(j, l, -1):  
        # iterate from end of left half to start of left half

        if a[i] != x and a[k] == x:  
                # compare element with pivot and ensure that swap is made with an element that = pivot

            a[k], a[i] = a[i], a[k]  # swap
            k += 1  # look at next element

        else:  # all elements from here on will be equal to pivot --> no swap needed
            break

    print('sorted', a[l:r + 1])
    print(equal_x, "values equal to pivot")
    return j, equal_x

def partition_finally(a, l, r):
    pivot = a[l]
    i, j, k = l, l, r 
    while i <= k:

        if a[i] < pivot:
            
            swap(a, i, j)
            j += 1
            i +=1
        elif a[i] > pivot:
            
            swap(a, i, k)
            k -= 1
        else:
            i+=1

    return j, k

def hoares_partition(a, l, r):
    i = l - 1
    j = r + 1

    pivot = a[l]

    while True:
        while True:
            i += 1
            if a[i] >= pivot:
                break

        while True:
            j -= 1
            if a[j] <= pivot:
                break

        if i >= j:
            return j

        a[i], a[j] = a[j], a[i]


def partition2(a, l, r):
    x = a[l]  # select pivot element (for comparision)

    # point to pivot
    j = l

    # iterate through (sub) array
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            # element is <= pivot --> swap with the end of the left half (sub) array
            # (ignoring the pivot and any previously swapped elements)
            j += 1  # extend the left half
            a[i], a[j] = a[j], a[i]  # swap

    # swap pivot to its correct position
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    # choose a pivot
    k = random.randint(l, r)

    # swap pivot with first element
    a[l], a[k] = a[k], a[l]

    #use partition3
    # m = hoares_partition(
    #     a, l, r
    # )  
    m1, m2 = partition_finally(
        a, l, r
    )  
    randomized_quick_sort(a, l, m1 - 1)
    # recurse into further sub arrays
    randomized_quick_sort(a, m2 + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

    ### STRESS TEST

    # import random
    # while True:
    #     print("\nSTART TEST")

    #     n = random.randint(10000, 10000)
    #     a = []
    #     for i in range(n):
    #         a.append(random.randint(0, 5))
    #     print("testing", a)

    #     a_copy = a.copy()
    #     res = randomized_quick_sort(a_copy, 0, len(a) - 1)
    #     correct = sorted(a)
    #     print('res\n', a_copy)
    #     print(correct)
    #     if a_copy != correct:
    #         print('incorrect')
    #         break

    ### END STRESS TEST
