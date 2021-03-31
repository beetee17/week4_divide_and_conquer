#Uses python3
import sys
import math
from itertools import combinations
import bisect

class KeyWrapper:
    def __init__(self, iterable, key):
        self.it = iterable
        self.key = key

    def __getitem__(self, i):
        return self.key(self.it[i])

    def __len__(self):
        return len(self.it)

def calc_dist(p1, p2):
    x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


def min_dist(points, points_y):
    # declare constnts for brevity
    X = 0
    Y = 1
    # recurse into two halves, s1 and s2
    mid = len(points) // 2

    # points have been sorted by x coordinate before function call

    # terminate recursion once sub arrays are small enough
    if len(points) < 4:
        return naive_min_dist(points)

    # get x coordinate of the middle point 
    mid_x = points[mid][X]

    
    # split array by middle x coordinate instead of length-wise 
    # to allow for y-sorted points to be generated accordingly without resorting 

    s1 = []
    equal_x = []

    i = 0

    # linear scan through less than entire list as it is presorted by x coordinate
    while points[i][X] < mid_x:
        s1.append(points[i])
        i += 1

    while points[i][X] == mid_x:
        equal_x.append(points[i])
        i += 1
        if i == len(points):
            break

    # remaining points are of coordinate > mid_x
    # divide the points with x = mid_x equally (if len > 1) among the two halves
    s1 += equal_x[:len(equal_x) // 2]
    s2 = equal_x[len(equal_x) // 2:] + points[i:]

    # filter the y sorted list
    s1_y = [point for point in points_y if point[X] < mid_x]
    s2_y = [point for point in points_y if point[X] > mid_x]

    # find appropriate index in log time for each point 
    # with x = mid_x to be inserted in the y sorted array
    
    for item in equal_x[:len(equal_x) // 2]:
        insert_index = bisect.bisect_left(KeyWrapper(s1_y, key= lambda point: point[Y]), item[Y])
        s1_y.insert(insert_index, item)


    for item in equal_x[len(equal_x) // 2:]:
        insert_index = bisect.bisect_left(KeyWrapper(s2_y, key= lambda point: point[Y]), item[Y])
        s2_y.insert(insert_index, item)

    # find min distances betwwen 2 points within s1 and s2
    d1 = min_dist(s1, s1_y)
    d2 = min_dist(s2, s2_y)

    # get the true minimum
    d = min(d1, d2)

    # filter points that are withtin d units of the mid-line 
    # points_y has been pre-sorted by y coordinate
    points = [point for point in points_y if point[X] > (mid_x - d) and point[X] < (mid_x + d)] 
                   


    minimum_dist = d

    # Using sparsity property of the scenario, 
    # only check the next 7 points (in increasing y coordinate) for each point
    for i in range(len(points)):
        for j in range(1, min(8, len(points) - i)):
            
            if abs(points[i][Y] - points[i+j][Y]) < d:
                
                dist = calc_dist(points[i], points[i+j])
                if dist < minimum_dist:
                    minimum_dist = dist
            else:
                # terminate inner loop as points are in ascending y values
                break

            

    return minimum_dist


def naive_min_dist(points):

    pairs = list(combinations(points, 2))

    min_dist = 10**10

    for pair in pairs:

        dist = calc_dist(pair[0], pair[1])

        if dist < min_dist:
            min_dist = dist

    return min_dist


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    points = [(x[i], y[i]) for i in range(n)]
    # sort points by x coordinate
    points = sorted(points, key=lambda x: x[0])
    points_y = sorted(points, key=lambda x: x[1])
    print("{0:.9f}".format(min_dist(points, points_y)))

    ### START STRESS TEST
    # import random
    # import time
    # while True:

    #     len_points = 100
    #     points = []

    #     range_ = 10
    #     for i in range(len_points):
    #         x = random.randint(-range_, range_)
    #         y = random.randint(-range_, range_)
    #         points.append((x, y))

    #     # sort points by x coordinate
    #     points = sorted(points, key=lambda point: point[0])
    #     points_y = sorted(points, key=lambda point: point[1])
    #     # print(points)
    #     print("START TEST, n =", len_points)
    #     # print("\nTEST POINTS", points)
    #     # print("\nTEST SEGMENTS",
    #     #       [(starts[i], ends[i]) for i in range(len_segments)])
    #     start = time.time()
    #     my_ans = min_dist(points, points_y)
    #     end = time.time()
    #     print("GOT RESULT, CHECKING...")
    #     print("my answer", my_ans)
    #     print("time taken", end - start)
    #     correct_ans = naive_min_dist(points)

    #     print("correct", correct_ans)

        

    #     if my_ans != correct_ans:
    #         print("INCORRECT")
    #         print(points)
    #         break
    #     print("PASSED")
