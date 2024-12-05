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


def check_print(rules, print_):
    """Check if the print is valid"""
    for index, page1 in enumerate(print_):
        for page2 in print_[index + 1 :]:
            if [page2, page1] in rules:
                return False
    return True


def reorder(print_, rules):
    """Reorder the print"""
    order_ok = False
    while not order_ok:
        order_ok = True
        for index, page1 in enumerate(print_):
            for page2 in print_[index + 1 :]:
                if [page2, page1] in rules:
                    print_[index], print_[index + 1] = print_[index + 1], print_[index]
                    order_ok = False
                    break
    return print_


def puzzles(filename):
    """Print Queue part 1 and 2"""
    rules, prints = read_and_parse(filename)
    total_good = total_bad = 0
    for print_ in prints:
        if check_print(rules, print_):
            total_good += print_[len(print_) // 2]
        else:
            reordered = reorder(print_, rules)
            total_bad += reordered[len(reordered) // 2]
    return total_good, total_bad


if __name__ == "__main__":
    result = puzzles("day_05_input_test.txt")
    print(result)
    result = puzzles("day_05_input_a.txt")
    print(result)

############################################
