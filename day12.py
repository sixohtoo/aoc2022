from pprint import pprint

def part1():
    with open("day12.txt") as f:
        lines = f.readlines()

    dirs = (
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    )

    for i,row in enumerate(lines):
        for j,c in enumerate(row):
            if c == 'S':
                start = (i, j)
            if c == 'E':
                end = (i, j)

    grid = [list(map(ord, list(line.strip()))) for line in lines]



    grid[start[0]][start[1]] = 999999
    grid[end[0]][end[1]] = ord('z')

    # really big number
    dist = [[999999 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    num_rows = len(grid)
    num_cols = len(grid[0])


    steps = 1
    queue = [start, 'step']
    while queue:
        node = queue.pop(0)

        if node == 'step':
            if not queue:
                break
            steps += 1
            queue.append('step')
            continue

        src_height = grid[node[0]][node[1]]

        for dir in dirs:
            dest = (node[0] + dir[0], node[1] + dir[1])
            dest_height = grid[dest[0]][dest[1]] if in_grid(dest, num_rows, num_cols) else 999999999999
            if dest_height <= src_height + 1 and steps < dist[dest[0]][dest[1]]:
                queue.append(dest)
                dist[dest[0]][dest[1]] = steps

    dist[start[0]][start[1]] = 'S'
    print(dist[end[0]][end[1]])
    pprint(dist)


def part2():
    with open("day12.txt") as f:
        lines = f.readlines()

    dirs = (
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    )

    for i,row in enumerate(lines):
        for j,c in enumerate(row):
            if c == 'S':
                start = (i, j)
            if c == 'E':
                end = (i, j)

    grid = [list(map(ord, list(line.strip()))) for line in lines]



    grid[start[0]][start[1]] = 999999
    grid[end[0]][end[1]] = ord('z')

    # really big number
    dist = [[999999 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    num_rows = len(grid)
    num_cols = len(grid[0])


    steps = 1
    queue = []
    for i, row in enumerate(grid):
        for j, height in enumerate(row):
            if height == ord('a'):
                queue.append((i, j))

    queue.append('step')
    while queue:
        node = queue.pop(0)

        if node == 'step':
            if not queue:
                break
            steps += 1
            queue.append('step')
            continue

        src_height = grid[node[0]][node[1]]

        for dir in dirs:
            dest = (node[0] + dir[0], node[1] + dir[1])
            dest_height = grid[dest[0]][dest[1]] if in_grid(dest, num_rows, num_cols) else 999999999999
            if dest_height <= src_height + 1 and steps < dist[dest[0]][dest[1]]:
                queue.append(dest)
                dist[dest[0]][dest[1]] = steps

    dist[start[0]][start[1]] = 'S'
    print(dist[end[0]][end[1]])



def in_grid(coord, num_rows, num_cols):
    if coord[0] < 0 or coord[1] < 0:
        return False
    if coord[0] >= num_rows or coord[1] >= num_cols:
        return False

    return True

if __name__ == '__main__':
    part1()
    part2()