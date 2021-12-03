def binary_common():
    file = open("inputs/input3.txt").readlines()
    epsilon = ''
    gamma = ''
    counter = 0

    while counter < 12:
        one = 0
        zero = 0
        for line in file:
            if line[counter] == '1':
                one += 1
            elif line[counter] == '0':
                zero += 1
        if one > zero:
            gamma = gamma + "1"
            epsilon = epsilon + "0"
        else:
            gamma = gamma + "0"
            epsilon = epsilon + "1"
        counter += 1
    return int(epsilon, 2) * int(gamma, 2)
