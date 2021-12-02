def travel2():
    file = open("../adventofcode2021/input2.txt").readlines()
    horizontal = 0
    depth = 0
    aim = 0

    for line in file:
        destination = line.split(' ')[0]
        amount = line.split(' ')[1]
        if destination == 'forward':
            horizontal += int(amount)
            depth += aim * int(amount)
        elif destination == 'up':
            aim -= int(amount)
        elif destination == 'down':
            aim += int(amount)
    return horizontal * depth