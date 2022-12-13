def part1():
    with open("day6.txt") as f:
        line = f.readline()

    num_unique = 4
    low = 0
    high = num_unique
    while len(set(line[low:high])) != num_unique:
        low += 1
        high += 1

    print(high)

def part2():
    with open("day6.txt") as f:
        line = f.readline()

    num_unique = 14
    low = 0
    high = num_unique
    while len(set(line[low:high])) != num_unique:
        low += 1
        high += 1
    print(high)

def part1_1line():
    with open("day6.txt") as f:
        line = f.readline()

    print([i + 4 for i,x in enumerate(line) if len(set(line[i:i+4])) == 4][0])

def part2_1line():
    with open("day6.txt") as f:
        line = f.readline()

    print([i + 14 for i,x in enumerate(line) if len(set(line[i:i+14])) == 14][0])

if __name__ == '__main__':
    part1()
    part2()