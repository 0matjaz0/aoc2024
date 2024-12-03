"""AOC 2024 day 2"""


def first_puzzle(filename):
    """Red-Nosed Reports part 1"""
    with open(filename, "r") as f:
        data = f.readlines()
    total_safe = 0
    for line in data:
        report = line.strip().split()
        report = [int(num) for num in report]
        trend = [report[i + 1] - report[i] for i in range(len(report) - 1)]
        safe = (all(num > 0 for num in trend) or all(num < 0 for num in trend)) and all(
            abs(num) <= 3 for num in trend
        )
        if safe:
            total_safe += 1
    return total_safe


def second_puzzle(filename):
    """Red-Nosed Reports part 2"""
    with open(filename, "r") as f:
        data = f.readlines()
    total_safe = 0
    for line in data:
        report = line.strip().split()
        report = [int(num) for num in report]
        trend = [report[i + 1] - report[i] for i in range(len(report) - 1)]
        safe = (all(num > 0 for num in trend) or all(num < 0 for num in trend)) and all(
            abs(num) <= 3 for num in trend
        )
        if safe:
            total_safe += 1
    return total_safe


if __name__ == "__main__":
    result = first_puzzle("day_02_input_test.txt")
    print(result)
    result = first_puzzle("day_02_input_a.txt")
    print(result)
#    result = second_puzzle("day_02_input_test.txt")
#    print(result)
#    result = second_puzzle("day_02_input_b.txt")
#    print(result)
