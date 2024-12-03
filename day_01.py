"""AOC 2024 day 1"""

def first_puzzle(filename):
    """Historian Hysteria part 1"""
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

def second_puzzle(filename):
    """Historian Hysteria part 2"""
    with open(filename, "r") as f:
        data = f.readlines()
    first_list = []
    second_list = []
    similarity_list = 0  
    for line in data:
        numbers = line.strip().split()
        first_list.append(int(numbers[0]))
        second_list.append(int(numbers[1]))
    similarity_list = [second_list.count(first_list[i]) * first_list[i] \
                       for i in range(len(first_list))]
    return sum(similarity_list)

if __name__ == "__main__":
    result = first_puzzle("day_01_input_a.txt")
    print(result)
    # result = second_puzzle("day_01_input_test.txt")
    result = second_puzzle("day_01_input_b.txt")
    print(result)


