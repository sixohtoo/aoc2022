from pprint import pprint

def part1():
    with open("day10.txt") as f:
        lines = f.readlines()

    x = 1
    cycle = 1
    target = 20 
    total = []
    for line in lines:
        if cycle == target:
            total.append(x * target)
            target += 40
        if line.startswith('noop'):
            cycle += 1
        else:
            cycle += 1
            if cycle == target:
                total.append(x * target)
                target += 40
            cycle += 1
            x += int(line.split()[1])

    print(sum(total[:6]))

def part2():
    with open("day10.txt") as f:
        lines = f.readlines()

    x = 1

    row = 0
    col = 0
    canvas = [['.' for _ in range(40)] for _ in range(6)]


    for line in lines:

        
        if line.startswith('noop'):
            if abs(col - x) <= 1:
                canvas[row][col] = '#'
            col += 1
        else:
            num = int(line.split()[1])
            if abs(col - x) <= 1:
                canvas[row][col] = '#'
            col += 1
            if col == 40:
                col = 0
                row += 1
            if abs(col - x) <= 1:
                canvas[row][col] = '#'
            col += 1
            x += int(line.split()[1])

        if col == 40:
            col = 0
            row += 1
        


    for x in canvas:
        print(''.join(x))

if __name__ == '__main__':
    part1()
    part2()