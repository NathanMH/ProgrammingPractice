path = "/home/natha/Documents/python/AdventOfCode/assets/Day10.txt"


outlet = 0


def read_input(filePath):

    with open(filePath, "r") as f:
        numbers = [0] + sorted([int(x) for x in f.readlines()])
    return numbers


def find_jolt_diff(val1, val2):
    return val2 - val1


def find_1x3(adpts):
    counts = {1: 0, 2: 0, 3: 1}
    for i in range(len(adpts) - 1):
        diff = find_jolt_diff(adpts[i], adpts[i + 1])
        counts[diff] += 1
    return counts[1] * counts[3]


def find_paths(adpts):
    possibilities = {adpts[-1]: 1}
    print(possibilities)
    for a in reversed(adpts[:-1]):
        possibilities[a] = sum(possibilities.get(x, 0) for x in (a + 1, a + 2, a + 3))
    print(possibilities[0])


def main():
    adapters = read_input(path)

    # print(find_1x3(adapters))
    find_paths(adapters)


if __name__ == "__main__":
    main()
