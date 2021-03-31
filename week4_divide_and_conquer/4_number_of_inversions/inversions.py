# Uses python3
import sys



def countInversions(a):
    """An inversion of a sequence 𝑎0,𝑎1,...,𝑎𝑛−1 is a pair of indices 0 ≤ 𝑖 < 𝑗 < 𝑛 such that 𝑎𝑖 > 𝑎𝑗. 
    The number of inversions of a sequence in some sense measures how close the sequence is to being 
    sorted. For example, a sorted (in non-descending order) sequence contains no inversions at all,
    while in a sequence sorted in de- scending order any two elements constitute an inversion 
    (for a total of 𝑛(𝑛 − 1)/2 inversions).
        
    Task 
    The goal in this problem is to count the number of inversions of a given sequence.

    Input Format
    The first line contains an integer 𝑛, the next one contains a sequence of integers
    𝑎0,𝑎1,...,𝑎𝑛−1.

    Constraints 
    1 ≤ 𝑛 ≤ 10^5
    1 ≤ 𝑎𝑖 ≤ 10^9 for all 0 ≤ 𝑖 < 𝑛

    Output Format 
    Output the number of inversions in the sequence."""
    
    if len(a) > 1:
        mid = len(a) // 2
        a_l = a[:mid]
        a_r = a[mid:]

        inv_l = countInversions(a_l)
        inv_r = countInversions(a_r)
        inv = inv_l + inv_r

        i = j = k = 0

        # print("unmerged arrs", a_l, a_r)

        while k < len(a):
            if i < len(a_l) and j < len(a_r):

                # print("comparing", a_l[i], "to", a_r[j])
                if a_l[i] < a_r[j]:
                    # first half smaller than second half. No split inversion
                    # sorted_a.append(a_l[i])
                    a[k] = a_l[i]
                    i += 1
                    k += 1

                elif a_r[j] < a_l[i]:
                    # first half is bigger than second half. i.e split inversion(s) found

                    a[k] = a_r[j]
                    inv += len(a_l) - i

                    j += 1
                    k += 1

                else:
                    # draw
                    a[k] = a_l[i]
                    a[k+1] = a_r[j]

                    i = min(i+1, len(a_l)-1)

                    if a_r[j] < a_l[i]:

                        inv += 1

                    j += 1
                    k += 2

            elif i < len(a_l):
                # selecting leftover values, if any
                a[k] = a_l[i]
                i += 1
                k += 1

            elif j < len(a_r):
                a[k] = a_r[j]
                j += 1
                k += 1

        # print("merged arr", a)
        return inv
    else:
        return 0






if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    # print(get_number_of_inversions(a, b, 0, len(a)))
    inv = countInversions(a)
    print(inv)