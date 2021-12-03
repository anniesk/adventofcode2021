def sliding_count():
    file = open('../inputs/input.txt').readlines()
    count = 0
    file_array = []
    prev_sum = 0
    current_sum = 0

    for i in file:
        file_array.append(i)

    while len(file_array) > 3:
        prev_sum = int(file_array[0]) + int(file_array[1]) + int(file_array[2])
        current_sum = int(file_array[1]) + int(file_array[2]) + int(file_array[3])
        if prev_sum < current_sum:
            count += 1
        file_array = file_array[1:]
    return count