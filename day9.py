from pprint import pprint

def part1():
    with open("day9.txt") as f:
        lines = f.readlines()

    dirs = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0)
    }

    head = (0, 0)
    tail = (0, 0)

    locations = set()
    locations.add((0,0))


    for line in lines:
        line = line.split()
        dir = dirs[line[0]]
        amount = int(line[1])

        for i in range(amount):
            head = (head[0] + dir[0], head[1] + dir[1])

            tail = towards(head, tail)
            locations.add(tail)

    print(len(locations))

def part2():
    with open("day9.txt") as f:
        lines = f.readlines()

    dirs = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0)
    }

    snake = [(0,0) for _ in range(10)]


    locations = set()
    locations.add((0,0))
    for line in lines:
        line = line.split()
        dir = dirs[line[0]]
        amount = int(line[1])

        for _ in range(amount):
            snake[0] = (snake[0][0] + dir[0], snake[0][1] + dir[1])
            for index, body in enumerate(snake[1:], start=1):
                snake[index] = towards(snake[index - 1], snake[index])
                locations.add(snake[-1])

    print(len(locations))





def distance(head, tail):
    return abs(head[0] - tail[0]), abs(head[1] - tail[1])

def towards(head, tail):
    d = distance(head, tail)

    if d[0] <= 1 and d[1] <= 1:
        return tail

    if head[0] == tail[0]:
        inc = 1 if head[1] > tail[1] else -1
        return (head[0], tail[1] + inc)
    if head[1] == tail[1]:
        inc = 1 if head[0] > tail[0] else -1
        return (tail[0] + inc, tail[1])
    else:
        tail = list(tail)
        if head[0] > tail[0]:
            tail[0] += 1
        else:
            tail[0] -= 1

        if head[1] > tail[1]:
            tail[1] += 1
        else:
            tail[1] -= 1
        return tuple(tail)






if __name__ == '__main__':
    part1()
    part2()