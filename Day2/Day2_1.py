def travel():
    file = open("../adventofcode2021/input2.txt").readlines()
    horizontal = 0
    depth = 0

    for line in file:
        destination = line.split(' ')[0]
        amount = line.split(' ')[1]
        if destination == 'forward':
            horizontal += int(amount)
        elif destination == 'up':
            depth -= int(amount)
        elif destination == 'down':
            depth += int(amount)
    return horizontal * depth