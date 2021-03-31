# Uses python3
import sys


def binary_search(a, low, high, x):
    """ The goal in this code problem is to implement the binary search algorithm.
    Input Format. 
    The first line of the input contains an integer 𝑛 and a sequence 
    𝑎0 < 𝑎1 < . . . < 𝑎𝑛−1 of 𝑛 pairwise distinct positive integers in increasing order. 
    The next line contains an integer 𝑘 and 𝑘 positive integers 𝑏0, 𝑏1, . . . , 𝑏𝑘−1.
    Constraints 
    1 ≤ 𝑘 ≤ 10^5
    1 ≤ 𝑛 ≤ 3·10^4
    1 ≤ 𝑎𝑖 ≤ 10^9 for all 0 ≤ 𝑖 <𝑛 
    1 ≤ 𝑏𝑗 ≤ 10^9 for all 0 ≤ 𝑗 < 𝑘
    Output Format
    For all 𝑖 from 0 to 𝑘−1, output an index 0 ≤ 𝑗 ≤ 𝑛−1 such that 𝑎𝑗 =𝑏𝑖 or−1 if there
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