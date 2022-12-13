from pprint import pprint
from collections import Counter

def part1():
    with open("day11.txt") as f:
        lines = f.readlines()

    # remove empty lines
    lines = [line for line in lines if line != "\n"]

    monkeys = {}

    total = Counter()


    for chunk in chunks(lines):
        num = chunk[0].split()[1][:-1]
        monkey = {}
        monkey['items'] = list(map(int, chunk[1].split(':')[1].split(',')))
        monkey['operation'] = chunk[2].split('=')[1].strip().replace('old', 'item')
        monkey['test'] = int(chunk[3].split()[-1])
        monkey[True] = chunk[4].split()[-1]
        monkey[False] = chunk[5].split()[-1]

        monkeys[num] = monkey


    for _ in range(20):
        for name, monkey in monkeys.items():
            while monkey['items']:
                # item is used in eval... (really dodgy)
                total[name] += 1 

                item = monkey['items'].pop(0)
                worry = eval(monkey['operation']) // 3
                outcome = worry % monkey['test'] == 0

                monkeys[monkey[outcome]]['items'].append(worry)
    
    for name, monkey in monkeys.items():
        print(name, monkey['items'])

    pprint(total)

    x = sorted(list(total.values()))

    print(x[-1] * x[-2])

def part1():
    with open("day11.txt") as f:
        lines = f.readlines()

    # remove empty lines
    lines = [line for line in lines if line != "\n"]

    monkeys = {}

    total = {}

    fear = 1

    for chunk in chunks(lines):
        num = chunk[0].split()[1][:-1]
        monkey = {}
        monkey['items'] = list(map(int, chunk[1].split(':')[1].split(',')))
        monkey['operation'] = chunk[2].split('=')[1].strip().replace('old', 'item')
        monkey['test'] = int(chunk[3].split()[-1])
        monkey[True] = chunk[4].split()[-1]
        monkey[False] = chunk[5].split()[-1]
        fear *= monkey['test']

        monkeys[num] = monkey

    pprint(monkeys)

    for i in range(10000):
        for name, monkey in monkeys.items():
            while monkey['items']:
                if name in total:
                    total[name] += 1
                else:
                    total[name] = 1

                item = monkey['items'].pop(0)
                worry = eval(monkey['operation']) % fear
                outcome = worry % monkey['test'] == 0

                monkeys[monkey[outcome]]['items'].append(worry)
    
    for name, monkey in monkeys.items():
        print(name, monkey['items'])

    pprint(total)

    x = sorted(list(total.values()))

    print(x[-1] * x[-2])



def chunks(iterable):
    i = iter(iterable)
    while True:
        try:
            yield next(i), next(i), next(i), next(i), next(i), next(i)
        except StopIteration:
            break


if __name__ == '__main__':
    part1()