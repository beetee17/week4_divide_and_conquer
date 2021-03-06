# Uses python3
import sys


def binary_search(a, low, high, x):
    """ The goal in this code problem is to implement the binary search algorithm.
    Input Format. 
    The first line of the input contains an integer π and a sequence 
    π0 < π1 < . . . < ππβ1 of π pairwise distinct positive integers in increasing order. 
    The next line contains an integer π and π positive integers π0, π1, . . . , ππβ1.
    Constraints 
    1 β€ π β€ 10^5
    1 β€ π β€ 3Β·10^4
    1 β€ ππ β€ 10^9 for all 0 β€ π <π 
    1 β€ ππ β€ 10^9 for all 0 β€ π < π
    Output Format
    For all π from 0 to πβ1, output an index 0 β€ π β€ πβ1 such that ππ =ππ orβ1 if there
    is no such index."""


    mid = (low + high) // 2
    # print('low', low, '\nhigh', high)
    # print('mid', mid)
    if low > high:

        return -1

    if x == a[mid]:
        # print('found at', mid)

        return mid

    elif x < a[mid]:
        # print(x, '<', a[mid])
        return binary_search(a, low, mid - 1, x)

    else:
        # print(x, '>', a[mid])
        return binary_search(a, mid + 1, high, x)


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    # import random
    # while True:
    #     n = random.randint(1, 20)
    #     a = []
    #     x = []
    #     for i in range(n):
    #         a.append(random.randint(1, 99))
    #         x.append(random.randint(1, 99))
    #     a = sorted(a)
    for x in data[n + 2:]:
    #     for i in x:
            # replace with the call to binary_search when implemented
        # print(linear_search(a, x), end=' ')
        print(binary_search(a, 0, len(a) - 1, x), end=' ')
# 5 1 5 8 12 13 
# 5 8 1 23 1 11
# 5 1 2 3 4 5
# 5 1 2 3 4 5