from Day1.Day1_1 import increased
from Day1.Day1_1 import count_increased
from Day1.Day1_2 import sliding_count
from Day2.Day2_2 import travel2
from Day2.Day2_1 import travel
from Day3.Day3_1 import binary_common
from Day3.Day3_2 import *

if __name__ == '__main__':
    print("Day 1")
    print(count_increased())
    print(increased())
    print(sliding_count())
    print("Day 2")
    print(travel())
    print(travel2())
    print("Day 3")
    print(binary_common())
    print("-------------------")
    print(part2("oxygen"), part2("life"))
    print(int(part2("oxygen"), 2) * int(part2("life"), 2))
    file = open("inputs/input3.txt").readlines()
    print(int(part2cleaner("oxygen"), 2) * int(part2cleaner("life"), 2))
    print(int(part2recursive(file, 0, "oxygen"), 2) * int(part2recursive(file, 0, "life"), 2))
