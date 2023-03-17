path = "/home/natha/Documents/python/AdventOfCode/assets/Day8.txt"


def read_input(path):
    # turn it into instructions

    commands = []
    with open(path, "r") as f:
        for line in f:
            lineSplit = line.strip().split()
            commands.append((lineSplit[0], int(lineSplit[1])))
    return commands


def execute(cmds):
    looped = False
    visited = set()
    key = 0
    accumulate = 0

    while key < len(cmds):
        k, v = cmds[key]

        if key in visited:
            looped = True
            break
        visited.add(key)

        if k == "jmp":
            key = key + v
            continue
        elif k == "acc":
            accumulate += v

        key += 1

    return (accumulate, looped)


# part 2
def swap(cmds):

    swapDict = {"nop": "jmp", "jmp": "nop"}
    for i, (op, value) in enumerate(cmds):
        if op == "nop" or op == "jmp":
            swappedOp = [(swapDict[op], value)]
            newInstructions = cmds[:i] + swappedOp + cmds[i + 1 :]
            accValue, hasLoop = execute(newInstructions)
            if not hasLoop:
                print(f"Part 2\n{accValue}")


def main():
    parsed = read_input(path)
    # print(parsed[0])

    swap(parsed)


if __name__ == "__main__":
    main()
