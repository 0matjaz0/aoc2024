"""AOC 2024 day 5"""


def read_and_parse(filename):
    """Read and parse the input file"""
    with open(filename, "r") as f:
        data = f.readlines()
    rules, prints = [], []
    for line in data:
        line = line.strip()
        if "|" in line:
            numbers = line.split("|")
            numbers = [int(num) for num in numbers]
            rules.append(numbers)
        elif "," in line:
            numbers = line.split(",")
            numbers = [int(num) for num in numbers]
            prints.append(numbers)
    return rules, prints


def check_print(rules, print):
    """Check if the print is valid"""
    for index, page in enumerate(print):
        # do something
    return False



def first_puzzle(filename):
    """Print Queue part 1"""
    rules, prints = read_and_parse(filename)
    print(rules)
    print(prints)
    return 0


if __name__ == "__main__":
    result = first_puzzle("day_05_input_test.txt")
    print(result)
#    result = first_puzzle("day_05_input_a.txt")
#    print(result)

############################################
