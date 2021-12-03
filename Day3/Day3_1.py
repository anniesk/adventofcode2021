def binary_common():
    file = open("../inputs/input3.txt").readlines()
    epsilon = ''
    gamma = ''

    for line in file:
        one = 0
        zero = 0
        for char in line:
            if char == '1':
                one += 1
            elif char == '0':
                zero += 1
        if one > zero:
            gamma = gamma + "1"
            epsilon = epsilon + "0"
        else:
            gamma = gamma + "0"
            epsilon = epsilon + "1"
    return epsilon, gamma
