def count_increased():
    with open('../inputs/input.txt') as f:
        file = f.readlines()

    count = 0
    line_number = 1
    prev_line = 0
    for current_line in file:
        if line_number == 1:
            line_number += 1
            prev_line = int(current_line)
            continue
        if int(current_line) >= prev_line:
            count += 1

        prev_line = int(current_line)
        line_number += 1
    return count


def increased():
    file = open("../inputs/input.txt").readlines()
    count = 0
    temp = 0

    for line in file:
        if temp != 0:
            if temp < int(line):
                count += 1
        temp = int(line)
    return count
