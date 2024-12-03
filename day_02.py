"""AOC 2024 day 2"""


def first_puzzle(filename):
    """Red-Nosed Reports part 1"""
    with open(filename, "r") as f:
        data = f.readlines()
    first_list = []
    second_list = []
    for line in data:
        numbers = line.strip().split()
        first_list.append(int(numbers[0]))
        second_list.append(int(numbers[1]))
    first_list.sort()
    second_list.sort()
    diff_list = [abs(second_list[i] - first_list[i]) for i in range(len(first_list))]
    return sum(diff_list)


if __name__ == "__main__":
    result = first_puzzle("day_02_input_test.txt")
    print(result)
    result = first_puzzle("day_02_input_a.txt")
    print(result)
"""    result = second_puzzle("day_02_input_test.txt")
    print(result)
    result = second_puzzle("day_02_input_b.txt")
    print(result)"""
