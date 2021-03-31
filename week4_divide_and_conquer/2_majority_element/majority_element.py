# Uses python3
import sys

def get_majority_element(a):
    """Majority rule is a decision rule that selects the alternative which has a majority, 
    that is, more than half the votes. Given a sequence of elements 𝑎1, 𝑎2, . . . , 𝑎𝑛, 
    you would like to check whether it contains an element that appears more than 𝑛/2 times. 
    The goal in this code problem is to check whether an input sequence contains a majority element. 
    
    Input Format
    The first line contains an integer 𝑛, the next one contains a sequence of 𝑛 non-negative
    integers 𝑎0, 𝑎1, . . . , 𝑎𝑛−1

    Constraints 
    1 ≤ 𝑛 ≤ 10^5
    0 ≤ 𝑎𝑖 ≤ 10^9 for all 0 ≤ 𝑖 < 𝑛
    
    Output Format 
    Output 1 if the sequence contains an element that appears strictly more than 𝑛/2 times, 
    and 0 otherwise."""

    a = sorted(a)

    max_count = 0
    curr_count = 0
    curr_num = a[0]
    

    for num in a:
        if num == curr_num:
            curr_count += 1
            # increment count if element is same as previous
        else:
            if curr_count > max_count:
                # count terminates, check if count is better than current max
                max_count = curr_count

            # reset count to 1 (since we already looked at the different element)
            curr_count = 1

            # set the current element to the one for comparison
            curr_num = num

    # final check in case majority element ends the list
    if curr_count > max_count:
        max_count = curr_count

    # check if majority element was found
    if max_count > len(a) // 2:

        return 1

    return 0
    


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))

    print(get_majority_element(a))
