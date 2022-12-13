from pprint import pprint
from itertools import zip_longest
import json
from functools import cmp_to_key

def part1():
    with open("day13.txt") as f:
        lines = f.readlines()

    lines = [line for line in lines if line != "\n"]

    lines = list(map(json.loads, lines))

    correct = []

    for i, lists in enumerate(chunks(lines), start=1):
        left, right = lists
        if checker(left, right) == -1:
            correct.append(i)

    print(sum(correct))

def part2():
    with open("day13.txt") as f:
        lines = f.readlines()

    lines = [line for line in lines if line != "\n"]

    lines = list(map(json.loads, lines))

    lines.append([[2]])
    lines.append([[6]])

    lines.sort(key=cmp_to_key(checker))

    key = 1
    for i, line in enumerate(lines, start=1):
        if line == [[[[2]]]]:
            key *= i
        elif line == [[[[6]]]]:
            key *= i
        # if line == [[[2]]]:
        #     key *= i
        # elif line == [[[6]]]:
        #     key *= i

    print(key)


def checker(left, right):
    index = [0]
    left = [left]
    right = [right]

    while index:
        if len(left[-1]) <= index[-1] and len(right[-1]) <= index[-1]:
            # index[-1] += 1
            index.pop(-1)
            left.pop(-1)
            right.pop(-1)
            index[-1] += 1
            continue
        elif len(left[-1]) <= index[-1]:
            return -1
        elif len(right[-1]) <= index[-1]:
            return 1

        if isinstance(left[-1][index[-1]], list) and not isinstance(right[-1][index[-1]], list):
            right[-1][index[-1]] = [right[-1][index[-1]]]
        elif isinstance(right[-1][index[-1]], list) and not isinstance(left[-1][index[-1]], list):
            left[-1][index[-1]] = [left[-1][index[-1]]]

        if isinstance(left[-1][index[-1]], int) and isinstance(right[-1][index[-1]], int): #both ints
            if left[-1][index[-1]] > right[-1][index[-1]]:
                return 1
            elif left[-1][index[-1]] < right[-1][index[-1]]:
                return -1
            else:
                index[-1] += 1
                continue
        else: # both lists
            if len(left[-1]) <= index[-1] and len(right[-1]) <= index[-1]:
                index.pop(-1)
                left.pop(-1)
                right.pop(-1)
                index[-1] += 1
                continue
            elif len(left[-1]) <= index[-1]:
                return -1
            elif len(right[-1]) <= index[-1]:
                return 1
            
            left.append(left[-1][index[-1]])
            right.append(right[-1][index[-1]])
            index.append(0)


def checker_r(index, left, right):
    if len(left) <= index and len(right) <= index:
        return 0
    elif len(left) <= index:
        return -1
    elif len(right) <= index:
        return 1

    if isinstance(left[index], list) and not isinstance(right[index], list):
        right[index] = [right[index]]
    elif isinstance(right[index], list) and not isinstance(left[index], list):
        left[index] = [left[index]]

    if isinstance(right[index], int) and isinstance(left[index], int):

        if left[index] > right[index]:
            return 1
        elif left[index] < right[index]:
            return -1
        else:
            return checker_r(index + 1, left, right)
    else:
        if len(left) <= index and len(right) <= index:
            return
        elif len(left) <= index:
            return 1
        elif len(right) <= index:
            return -1
        status = checker_r(0, left[index], right[index])
        if status == -1:
            return -1
        elif status == 1:
            return 1
        else:
            return checker_r(index + 1, left, right)



def chunks(arr):
    i = iter(arr)
    while True:
        try:
            yield next(i), next(i)

        except StopIteration:
            break

if __name__ == '__main__':
    part1()
    part2()