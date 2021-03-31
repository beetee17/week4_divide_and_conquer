# Uses python3
import sys


def get_master_list(starts, ends, points):

    a = []
    starts_dict = {}
    ends_dict = {}
    points_dict = {}
    num_set = sorted(set(starts + ends + points))
    for num in num_set:
        starts_dict.update({num: 0})
        ends_dict.update({num: 0})
        points_dict.update({num: 0})

    for s in starts:
        starts_dict[s] += 1

    for p in points:
        points_dict[p] += 1

    for e in ends:
        ends_dict[e] += 1

    for num in num_set:
        for i in range(starts_dict[num]):
            a.append((num, 'l'))
        for i in range(points_dict[num]):
            a.append((num, 'p'))
        for i in range(ends_dict[num]):
            a.append((num, 'r'))
    return a


def fast_count_segments(starts, ends, points):
    a = get_master_list(starts, ends, points)

    cnt_dict = {}

    count = 0

    for item in a:
        if item[1] == 'l':
            count += 1

        elif item[1] == 'r':
            count -= 1

        elif item[1] == ('p'):
            cnt_dict.update({item[0]: count})

    return [cnt_dict[p] for p in points]


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n = data[0]
    # m = data[1]
    # starts = data[2:2 * n + 2:2]
    # ends = data[3:2 * n + 2:2]
    # points = data[2 * n + 2:]
    # #use fast_count_segments
    # cnt = fast_count_segments(starts, ends, points)
    # for x in cnt:
    #     print(x, end=' ')

    ### START STRESS TEST
    import random
    while True:

        len_points = random.randint(10000, 10000)
        len_segments = random.randint(10000, 10000)
        points = []
        starts = []
        ends = []
        range_ = (1, 20)
        for i in range(len_points):
            points.append(random.randint(range_[0], range_[1]))
        for i in range(len_segments):
            start = random.randint(range_[0], range_[1])
            end = random.randint(start, range_[1])

            starts.append(start)
            ends.append(end)
        print("START TEST")
        # print("\nTEST POINTS", points)
        # print("\nTEST SEGMENTS",
        #       [(starts[i], ends[i]) for i in range(len_segments)])
        my_cnt = fast_count_segments(starts, ends, points)
        print("GOT RESULT, CHECKING...")
        correct_cnt = naive_count_segments(starts, ends, points)

        # print("correct", correct_cnt)

        # print("my answer", my_cnt)

        if my_cnt != correct_cnt:
            print("INCORRECT")
            break
        print("PASSED")
