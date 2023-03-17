from itertools import combinations

path = "/home/natha/Documents/python/AdventOfCode/assets/Day9.txt"
preamble = 25


def read_input(path):
    """ Reads input file """

    xmas = []
    with open(path, "r") as f:
        for line in f:
            xmas.append(int(line))
    return xmas


def main():
    parsed = read_input(path)

    for i in range(preamble, len(parsed)):
        all_combos = combinations(parsed[i - preamble : i], 2)
        sums = [sum(x) for x in all_combos]
        if parsed[i] not in sums:
            answer1 = parsed[i]

    for i in range(2, len(parsed)):
        for j in range(1, len(parsed) - i):
            sum_of = sum(parsed[j : j + i])
            if sum_of == answer1:
                max_int = max(parsed[j : j + i])
                min_int = min(parsed[j : j + i])
                print(max_int + min_int)


if __name__ == "__main__":
    main()
