"""AOC 2024 day 4"""

import re


def count_xmas(strings):
    count = 0
    for string in strings:
        count += string.count("XMAS") + string.count("SAMX")
    return count


def first_puzzle(filename):
    """Ceres Search part 1"""
    total = 0
    with open(filename, "r") as f:
        data = f.readlines()
    table = []
    for line in data:
        line = line.strip()
        letters = list(line)
        table.append(letters)
    maxx, maxy = len(table[0]), len(table)
    m_table = table[::-1]  # mirror table
    #    print(maxx, maxy)
    diagonals = []
    m_diagonals = []
    for i in range(maxx + maxy - 1):
        diagonal = []
        m_diagonal = []
        for j in range(max(maxx, maxy)):
            if i - j >= 0 and i - j < maxy and j < maxx:
                diagonal.append(table[i - j][j])
                m_diagonal.append(m_table[i - j][j])
        diagonal_str = "".join(diagonal)
        diagonals.append(diagonal_str)
        m_diagonal_str = "".join(m_diagonal)
        m_diagonals.append(m_diagonal_str)
    increase = count_xmas(diagonals)
    m_increase = count_xmas(m_diagonals)
    total = increase + m_increase
    row_strings = ["".join(row) for row in table]
    total += count_xmas(row_strings)
    column_strings = ["".join(column) for column in zip(*table)]
    total += count_xmas(column_strings)

    return total


#    for i in range(len(diagonals)):
#        print(diagonals[i])


if __name__ == "__main__":
    result = first_puzzle("day_04_input_test.txt")
    print(result)

#    result = first_puzzle("day_04_input_a.txt")
#  print(result)

############################################
