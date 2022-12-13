from pprint import pprint
import json

def part1():
    with open("day7.txt") as f:
        lines = f.readlines()

    path = []
    
    """
    dirs contains list of file sizes/dir sizes in directionry

    ints are file sizes
    strings are names of directories which have a referencce in dirs
    e.g.
    dir['home'] = [1, 23, '/home/user', '/home/random']
    
    """
    dirs = {}
    for text in lines:
        line = text.split()
        
        # deal with commands
        if line[0] == '$':

            # Deal with cd
            if line[1] == 'cd':

                # Deal with cd /
                if line[2] == '/':
                    path = ['/']
                    dirs['/'] = []
                elif line[2] == '..':
                    path = path[:-1]
                # Deal with relative cd
                else:
                    path.append(line[2] + '/')
                    dirs[''.join(path)] = []
        
            # Don't care if running ls - doesn't change anything
        else:
            if line[0] == 'dir':
                dirs[''.join(path)].append(''.join(path) + line[1] + '/')
            else:
                dirs[''.join(path)].append(line[0])
    
    sizes = {}

    directories = list(dirs.keys())
    for dir in directories:
        if all(item.isnumeric() for item in dirs[dir]):
            sizes[dir] = sum(map(int, dirs[dir]))
        else:
            child_dirs = [x for x in dirs[dir] if not x.isnumeric()]
            if all(x in sizes for x in child_dirs):
                sizes[dir] = sum(int(x) if x.isnumeric() else sizes[x] for x in dirs[dir])
            else:
                directories.append(dir)

    print(sum(sizes[x] for x in sizes if sizes[x] <= 100000))


def part2():
    with open("day7.txt") as f:
        lines = f.readlines()

    path = []
    
    """
    dirs contains list of file sizes/dir sizes in directionry

    ints are file sizes
    strings are names of directories which have a referencce in dirs
    e.g.
    dir['home'] = [1, 23, '/home/user', '/home/random']
    
    """
    dirs = {}
    for text in lines:
        line = text.split()
        
        # deal with commands
        if line[0] == '$':

            # Deal with cd
            if line[1] == 'cd':

                # Deal with cd /
                if line[2] == '/':
                    path = ['/']
                    dirs['/'] = []
                elif line[2] == '..':
                    path = path[:-1]
                # Deal with relative cd
                else:
                    path.append(line[2] + '/')
                    dirs[''.join(path)] = []
        
            # Don't care if running ls - doesn't change anything
        else:
            if line[0] == 'dir':
                dirs[''.join(path)].append(''.join(path) + line[1] + '/')
            else:
                dirs[''.join(path)].append(line[0])
    
    sizes = {}

    directories = list(dirs.keys())
    for dir in directories:
        if all(item.isnumeric() for item in dirs[dir]):
            sizes[dir] = sum(map(int, dirs[dir]))
        else:
            child_dirs = [x for x in dirs[dir] if not x.isnumeric()]
            if all(x in sizes for x in child_dirs):
                sizes[dir] = sum(int(x) if x.isnumeric() else sizes[x] for x in dirs[dir])
            else:
                directories.append(dir)

    empty = 70000000 - sizes['/']
    clear = 30000000 - empty
    print(min(sizes[x] for x in sizes if sizes[x] >= clear))


if __name__ == '__main__':
    part1()
    part2()