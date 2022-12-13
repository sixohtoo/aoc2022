from pprint import pprint

def part1():
    with open("day8.txt") as f:
        lines = f.readlines()

    lines = list(map(lambda a: list(a.strip()), lines))
    visible = [[False for x in range(len(lines[0]))] for y in range(len(lines))]
    width = len(visible[0])
    height = len(visible)

    for i, line in enumerate(lines):
        line = list(map(int, line))
        rev = list(reversed(line))
        for j, n in enumerate(line):
            if i == 0 or j == 0 or i == height - 1 or j == width - 1: # will improve?
                visible[i][j] = True
            elif n > max(line[:j]):
                visible[i][j] = True
            elif n > max(rev[:width - 1 - j]):
                visible[i][j] = True

    for i in range(width):
        line = list(map(int,[lines[x][i] for x in range(height)]))
        rev = list(reversed(line))
        for j in range(height):
            n = int(lines[j][i])
            if visible[j][i]:
                continue
            elif n > max(line[:j]):
                visible[j][i] = True
            elif n > max(rev[:height - 1 - j]):
                visible[j][i] = True

    print(sum(map(sum, visible)))


def part2():
    with open("day8.txt") as f:
        lines = f.readlines()

    lines = list(map(lambda a: list(map(int,a.strip())), lines))

    score = [[0 for x in range(len(lines[0]))] for y in range(len(lines))]


    height = len(lines)
    width = len(lines[0])

    # # calculate right score
    for i, line in enumerate(lines):
        sizes = {}
        for j, n in enumerate(line):

            # calculate left score for unscored smaller or equal trees
            for x in range(n + 1):
                if x in sizes:
                    for index in sizes[x]:
                        score[i][index] = j - index
                    del sizes[x]
            if n in sizes:
                sizes[n].append(j)
            else:
                sizes[n] = [j]

        for size in sizes:
            for index in sizes[size]:
                score[i][index] = width - index - 1

    # calculate left score
    for i, line in enumerate(lines):
        sizes = {}
        for j, n in enumerate(reversed(line)):
            # calculate right score for unscored smaller or equal trees
            for x in range(n + 1):
                if x in sizes:
                    for index in sizes[x]:
                        score[i][width - index - 1] *= j - index
                    del sizes[x]
            if n in sizes:
                sizes[n].append(j)
            else:
                sizes[n] = [j]

        for size in sizes:
            for index in sizes[size]:
                score[i][width - 1 - index] *= width - index - 1


    lines = list(zip(*lines[::-1]))


    # # calculate up score
    for i, line in enumerate(lines):
        sizes = {}
        for j, n in enumerate(line):

            # calculate left score for unscored smaller or equal trees
            for x in range(n + 1):
                if x in sizes:
                    for index in sizes[x]:
                        score[height - index - 1][i] *= j - index
                    del sizes[x]
            if n in sizes:
                sizes[n].append(j)
            else:
                sizes[n] = [j]

        for size in sizes:
            for index in sizes[size]:
                score[height - index - 1][i] *= width - index - 1

    # calculate down score
    for i, line in enumerate(lines):
        sizes = {}
        for j, n in enumerate(reversed(line)):

            # calculate right score for unscored smaller or equal trees
            for x in range(n + 1):
                if x in sizes:
                    for index in sizes[x]:
                        score[index][i] *= j - index
                    del sizes[x]
            if n in sizes:
                sizes[n].append(j)
            else:
                sizes[n] = [j]

        for size in sizes:
            for index in sizes[size]:
                score[index][i] *= width - index - 1

    print(max(max(x) for x in score))





if __name__ == '__main__':
    part1()
    part2()

