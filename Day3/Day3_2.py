from collections import Counter


def part2(rating):
    file = open("inputs/input3.txt").readlines()

    for i in range(len(file[0])):
        common = Counter(line[i] for line in file)
        if rating == "life":
            if common['1'] >= common['0']:
                file = [line for line in file if line[i] == '0']
            if common['1'] < common['0']:
                file = [line for line in file if line[i] == '1']
        elif rating == "oxygen":
            if common['1'] < common['0']:
                file = [line for line in file if line[i] == '0']
            if common['1'] >= common['0']:
                file = [line for line in file if line[i] == '1']
        if len(file) == 1:
            return file[0]


def part2cleaner(rating):
    file = open("inputs/input3.txt").readlines()

    for i in range(len(file[0])):
        common = Counter(line[i] for line in file)
        if rating == "life":
            bit = '1' if common['1'] >= common['0'] else '0'
        elif rating == "oxygen":
            bit = '0' if common['1'] >= common['0'] else '1'
        file = [line for line in file if line[i] == bit]
        if len(file) == 1:
            return file[0]


def part2recursive(file, i, rating):
    if len(file) == 1:
        return file[0]
    common = Counter(line[i] for line in file)
    if rating == "life":
        bit = '1' if common['1'] >= common['0'] else '0'
    elif rating == "oxygen":
        bit = '0' if common['1'] >= common['0'] else '1'
    newFile = [line for line in file if line[i] == bit]
    return part2recursive(newFile, i+1, rating)