"""AOC 2024 day 3"""

import re


def first_puzzle(filename):
    """Mull It Over part 1"""
    with open(filename, "r") as f:
        data = f.readlines()
    sum_of_products = 0
    for line in data:
        line
        allcmds = re.finditer(r"mul\((\d{1,3})\,(\d{1,3})\)", line)
        for cmd in allcmds:
            a, b = int(cmd.group(1)), int(cmd.group(2))
            sum_of_products += a * b
    return sum_of_products


def second_puzzle(filename):
    """Mull It Over part 2"""
    with open(filename, "r") as f:
        data = f.readlines()
    sum_of_products = 0
    enabled = True
    for line in data:
        allcmds = re.finditer(r"mul\((\d{1,3})\,(\d{1,3})\)|do\(\)|don't\(\)", line)
        for cmd in allcmds:
            if cmd.group(0) == "do()":
                enabled = True
            elif cmd.group(0) == "don't()":
                enabled = False
            elif enabled:
                a, b = int(cmd.group(1)), int(cmd.group(2))
                sum_of_products += a * b
    return sum_of_products


if __name__ == "__main__":
    result = first_puzzle("day_03_input_test.txt")
    print(result)
    result = first_puzzle("day_03_input_a.txt")
    print(result)
    result = second_puzzle("day_03_input_test2.txt")
    print(result)
    result = second_puzzle("day_03_input_a.txt")
    print(result)

############################################
